import sys
import os
import time
import random
import sqlite3
import threading
import logging
from datetime import datetime

from flask import Flask, request, jsonify, render_template
from openai import OpenAI
from dotenv import load_dotenv
from werkzeug.serving import make_server
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

# ---------- 日志配置 ----------
if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS
    EXE_DIR = os.path.dirname(sys.executable)
else:
    BASE_DIR = os.path.abspath('.')
    EXE_DIR = BASE_DIR

LOG_FILE = os.path.join(EXE_DIR, 'debug.txt')
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logging.info("=== EchoCast 程序启动 ===")
logging.info(f"当前工作目录: {os.getcwd()}")
logging.info(f"EXE 所在目录: {EXE_DIR}")

# ---------- 加载环境变量 ----------
env_path = os.path.join(EXE_DIR, '.env')
if os.path.exists(env_path):
    load_dotenv(env_path)
    logging.info(f"已加载 .env 文件: {env_path}")
else:
    logging.warning(f"未找到 .env 文件: {env_path}")

# ---------- 初始化 Flask ----------
try:
    app = Flask(__name__, 
                template_folder=os.path.join(BASE_DIR, 'templates'))
    logging.info("Flask 应用初始化成功")
except Exception as e:
    logging.error(f"Flask 初始化失败: {e}")
    input("按回车键退出...")
    sys.exit(1)

# ---------- 初始化智谱 AI ----------
api_key = os.environ.get('ZHIPU_API_KEY')
if not api_key:
    logging.warning("未找到 ZHIPU_API_KEY，AI 功能将降级为原文输出")
else:
    logging.info("已读取到 ZHIPU_API_KEY (长度: {})".format(len(api_key)))

client = None
try:
    if api_key:
        client = OpenAI(
            api_key=api_key,
            base_url="https://open.bigmodel.cn/api/paas/v4/"
        )
        logging.info("OpenAI 客户端初始化成功")
except Exception as e:
    logging.error(f"OpenAI 客户端初始化失败: {e}")
    client = None

# ---------- 数据库 ----------
def get_db_path():
    user_docs = os.path.join(os.environ['USERPROFILE'], 'Documents', 'EchoCast')
    if not os.path.exists(user_docs):
        os.makedirs(user_docs)
        logging.info(f"创建数据库目录: {user_docs}")
    return os.path.join(user_docs, 'messages.db')

def get_db():
    conn = sqlite3.connect(get_db_path())
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    try:
        conn = get_db()
        conn.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original TEXT,
                poem TEXT,
                lat REAL,
                lng REAL,
                timestamp TEXT
            )
        ''')
        conn.commit()
        conn.close()
        logging.info("数据库初始化成功")
    except Exception as e:
        logging.error(f"数据库初始化失败: {e}")

# ---------- 路由 ----------
@app.route('/')
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        logging.error(f"渲染首页失败: {e}")
        return "页面加载失败，请查看 debug.txt", 500

@app.route('/check_api')
def check_api():
    """检测 API 是否可用"""
    if client is None:
        return jsonify({
            'available': False,
            'message': '未配置 ZHIPU_API_KEY，请先注册并配置密钥'
        })
    
    # 尝试调用 API 验证密钥是否有效
    try:
        test_response = client.chat.completions.create(
            model='glm-4-flash',
            messages=[{'role': 'user', 'content': '测试'}],
            max_tokens=1
        )
        return jsonify({'available': True})
    except Exception as e:
        error_msg = str(e)
        if 'Invalid API key' in error_msg or 'authentication' in error_msg.lower():
            return jsonify({
                'available': False,
                'message': 'API 密钥无效，请检查 .env 文件中的 ZHIPU_API_KEY 是否正确'
            })
        else:
            return jsonify({
                'available': False,
                'message': f'API 连接失败: {error_msg[:100]}'
            })

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.get_json()
        original = data.get('text', '').strip()
        if not original:
            return jsonify({'error': '内容不能为空'}), 400

        if client is not None:
            try:
                response = client.chat.completions.create(
                    model='glm-4-flash',
                    messages=[
                        {'role': 'system', 'content': '你是一个诗人，请将用户输入的内容改写成一首简短而有诗意的中文诗歌，不超过50字。'},
                        {'role': 'user', 'content': original}
                    ],
                    max_tokens=100
                )
                poem = response.choices[0].message.content.strip()
                logging.info(f"AI 生成成功: {poem[:20]}...")
            except Exception as e:
                logging.error(f"AI 调用失败: {e}")
                poem = original
        else:
            poem = original
            logging.warning("客户端未初始化，使用原文")

        lat = random.uniform(-90, 90)
        lng = random.uniform(-180, 180)
        timestamp = datetime.now().isoformat()

        conn = get_db()
        conn.execute(
            'INSERT INTO messages (original, poem, lat, lng, timestamp) VALUES (?, ?, ?, ?, ?)',
            (original, poem, lat, lng, timestamp)
        )
        conn.commit()
        conn.close()

        return jsonify({'success': True, 'poem': poem, 'lat': lat, 'lng': lng})
    except Exception as e:
        logging.error(f"submit 路由出错: {e}")
        return jsonify({'error': '服务器内部错误'}), 500

@app.route('/random')
def random_message():
    try:
        conn = get_db()
        cur = conn.execute('SELECT id FROM messages')
        ids = [row['id'] for row in cur.fetchall()]
        if not ids:
            conn.close()
            return jsonify({'error': '大海里还没有信，你先投一个吧'}), 404
        random_id = random.choice(ids)
        msg = conn.execute('SELECT * FROM messages WHERE id=?', (random_id,)).fetchone()
        conn.close()
        return jsonify({
            'id': msg['id'],
            'poem': msg['poem'],
            'lat': msg['lat'],
            'lng': msg['lng'],
            'timestamp': msg['timestamp']
        })
    except Exception as e:
        logging.error(f"random 路由出错: {e}")
        return jsonify({'error': '服务器内部错误'}), 500

@app.route('/shutdown')
def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func:
        func()
    logging.info("服务器已通过 /shutdown 关闭")
    return '🛑 服务器已关闭，你可以关闭浏览器了。'

# ---------- 启动入口（带 Qt 窗口，支持高 DPI 缩放）----------
if __name__ == '__main__':
    init_db()

    # 启动 Flask 服务器（独立线程）
    server = make_server('127.0.0.1', 5000, app)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    logging.info("Flask 服务器已启动于 http://127.0.0.1:5000")

    # 等待服务器就绪
    time.sleep(1.5)

    # ---------- 启用 Qt 高 DPI 缩放 ----------
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    qt_app = QApplication(sys.argv)
    qt_app.setStyleSheet("QMainWindow { background: #f0f7ff; }")

    # 根据屏幕尺寸自适应窗口大小（默认占屏幕 75% 宽度，80% 高度）
    screen = qt_app.primaryScreen()
    screen_size = screen.availableGeometry()
    win_width = int(screen_size.width() * 0.75)
    win_height = int(screen_size.height() * 0.80)

    window = QMainWindow()
    window.setWindowTitle("EchoCast · 漂流信")
    window.setGeometry(100, 100, win_width, win_height)

    browser = QWebEngineView()
    browser.load(QUrl("http://127.0.0.1:5000"))
    window.setCentralWidget(browser)

    def on_close(event):
        logging.info("窗口关闭，正在停止服务器...")
        server.shutdown()
        event.accept()

    window.closeEvent = on_close
    window.show()

    logging.info("Qt 窗口已显示，程序运行中...")
    sys.exit(qt_app.exec_())