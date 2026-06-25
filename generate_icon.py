from PIL import Image, ImageDraw, ImageFont
import os

# 创建 512x512 画布
size = 512
img = Image.new('RGB', (size, size), color='#0c4a6e')
draw = ImageDraw.Draw(img)

# ---------- 绘制海浪 ----------
wave_color = '#0ea5e9'
for i in range(0, size, 20):
    y = 400 + 30 * (i % 3) + 20
    draw.ellipse([(i-30, y-20), (i+50, y+20)], fill=wave_color, outline=None)

# ---------- 绘制漂流瓶主体 ----------
bottle_x, bottle_y = 256, 260
# 瓶身（梯形）
draw.polygon([
    (180, 180),   # 瓶口左上
    (220, 160),   # 瓶口右上
    (332, 160),   # 瓶颈右上
    (332, 180),   # 瓶颈右下
    (310, 320),   # 瓶身右下
    (202, 320),   # 瓶身左下
], fill='#dbeafe', outline='#93c5fd', width=3)

# ---------- 瓶中信纸 ----------
draw.rectangle([(220, 190), (292, 260)], fill='#fef3c7', outline='#fbbf24', width=2)

# ---------- 信纸上的文字（用线条模拟） ----------
draw.line([(230, 200), (282, 200)], fill='#b45309', width=2)
draw.line([(230, 210), (282, 210)], fill='#b45309', width=2)
draw.line([(230, 220), (272, 220)], fill='#b45309', width=2)

# ---------- 瓶塞 ----------
draw.rectangle([(240, 150), (272, 170)], fill='#92400e', outline='#78350f', width=2)

# ---------- 高光 ----------
draw.ellipse([(210, 180), (230, 200)], fill='#ffffff', outline=None)

# ---------- 添加文字（底部的“EchoCast”） ----------
try:
    # 尝试使用系统字体
    font = ImageFont.truetype("arial.ttf", 48)
except:
    font = ImageFont.load_default()

draw.text((140, 430), "EchoCast", fill='#f0f9ff', font=font)

# 保存
img.save('icon.png')
print("图标已生成: icon.png")