import sys
import os
import webbrowser
import time
import random
import sqlite3
from datetime import datetime
from flask import Flask, request, jsonify, render_template
from openai import OpenAI  # 使用 openai 库，但指向智谱的 API
from dotenv import load_dotenv

# ---------- 路径适配：支持开发环境和 EXE 打包 ----------
if getattr(sys, 'frozen', False):
    # 打包成 EXE 后，资源文件从 _MEIPASS 读取
    BASE_DIR = sys._MEIPASS
else:
    # 开发环境（python app.py）
    BASE_DIR = os.path.abspath('.')

# 加载 .env 文件（从 BASE_DIR 读取）
load_dotenv(os.path.join(BASE_DIR, '.env'))

# ---------- 初始化 Flask ----------
app = Flask(__name__, 
            template_folder=os.path.join(BASE_DIR, 'templates'))

# ---------- 初始化智谱 AI 客户端（使用 OpenAI 兼容接口）----------
client = OpenAI(
    api_key=os.environ.get('ZHIPU_API_KEY'),          # 从环境变量读取
    base_url="https://open.bigmodel.cn/api/paas/v4/"  # 智谱的 API 地址
)

# ---------- 数据库路径（存放在用户文档目录，避免 EXE 所在目录无写权限）----------
def get_db_path():
    user_docs = os.path.join(os.environ['USERPROFILE'], 'Documents', 'EchoCast')
    if not os.path.exists(user_docs):
        os.makedirs(user_docs)
    return os.path.join(user_docs, 'messages.db')

def get_db():
    conn = sqlite3.connect(get_db_path())
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
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

# ---------- 路由 ----------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    original = data.get('text', '').strip()
    if not original:
        return jsonify({'error': '内容不能为空'}), 400

    # 调用智谱 AI 将原文改写成诗
    try:
        response = client.chat.completions.create(
            model='glm-4-flash',  # 永久免费模型
            messages=[
                {'role': 'system', 'content': '你是一个诗人，请将用户输入的内容改写成一首简短而有诗意的中文诗歌，不超过50字。'},
                {'role': 'user', 'content': original}
            ],
            max_tokens=100
        )
        poem = response.choices[0].message.content.strip()
    except Exception as e:
        # 如果 API 调用失败（如网络问题或 Key 无效），降级为原文
        poem = original

    # 随机经纬度（全球范围）
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

@app.route('/random')
def random_message():
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

@app.route('/shutdown')
def shutdown():
    """关闭服务器的路由（用于无黑框模式下优雅退出）"""
    func = request.environ.get('werkzeug.server.shutdown')
    if func:
        func()
    return '🛑 服务器已关闭，你可以关闭浏览器了。'

# ---------- 启动入口 ----------
if __name__ == '__main__':
    init_db()
    # 延迟 1.5 秒打开浏览器，确保服务已启动
    time.sleep(1.5)
    webbrowser.open('http://127.0.0.1:5000')
    app.run(host='127.0.0.1', port=5000, debug=False)