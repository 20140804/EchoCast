# 🌊 EchoCast · 漂流信

> 不是社交，是偶遇。在赛博空间的海边，做一个扔瓶子的人。

[![GitHub stars](https://img.shields.io/github/stars/20140804/EchoCast)](https://github.com/20140804/EchoCast/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/20140804/EchoCast)](https://github.com/20140804/EchoCast/network)
[![GitHub license](https://img.shields.io/github/license/20140804/EchoCast)](https://github.com/20140804/EchoCast/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)

---

## 📖 简介

**EchoCast** 是一个轻量级的匿名诗意漂流瓶应用。你只需写下一瞬间的念头，AI（智谱 GLM-4-Flash）会将它重构成一首短诗，并随机抛掷在地球的某个经纬度坐标上。而另一个陌生人，可以通过地图，随机捞起这段来自远方的匿名回声。

**这个世界不缺效率工具，缺的是不期而遇的浪漫。**

## ✨ 核心功能

- 🗺️ **地图锚定**：每一封信都是一个真实世界地图上的坐标点。
- 🤖 **AI 赋诗**：使用智谱 AI 的免费模型 `glm-4-flash`，将大白话改写成有意境的短诗（**永久免费**）。
- 🎭 **绝对匿名**：不注册、不登录、不留痕，只有纯粹的文字偶遇。
- 📦 **开箱即用**：打包为独立的 EXE 桌面应用，双击即用，无需安装 Python。

## 🛠️ 技术栈

| 类别 | 技术 |
|------|------|
| 后端 | Python 3.8+ / Flask |
| AI 接口 | 智谱 AI (GLM-4-Flash) 兼容 OpenAI SDK |
| 前端地图 | Leaflet.js + OpenStreetMap |
| 桌面框架 | PyQt5 + QWebEngineView |
| 数据库 | SQLite（零配置，单文件） |
| 打包工具 | PyInstaller（生成独立 EXE） |

---

## 🚀 快速开始

### 第一步：下载软件

前往 [Releases](https://github.com/20140804/EchoCast/releases) 页面下载 `EchoCast.exe`。

### 第二步：获取免费的 API 密钥（关键步骤）

EchoCast 使用智谱 AI 的 `glm-4-flash` 模型，该模型**永久免费**。你只需要花 2 分钟注册并获取一个密钥。

1. 访问 [智谱AI开放平台](https://open.bigmodel.cn/) 注册账号。
2. 登录后，进入 **控制台** → **API Keys**。
3. 点击 **创建新的 API Key**，复制生成的密钥（格式为 `sk-xxxxxx`）。

### 第三步：配置密钥

1. 将 `EchoCast.exe` 放在一个独立的文件夹中。
2. 在**同一文件夹**中，创建一个名为 `.env` 的文件（注意文件名以点开头）。
3. 用记事本打开 `.env`，写入以下内容：
   ```
   ZHIPU_API_KEY=你的密钥ID
   ```
   将 `sk-你的密钥` 替换为刚才复制的真实密钥。

### 第四步：运行

双击 `EchoCast.exe`，软件会自动打开。首次运行时会检测密钥，如果未配置，会显示引导弹窗帮助你完成配置。

---

## 🧭 使用说明

| 操作 | 说明 |
|------|------|
| 写下心情 → 投入大海 | 输入文字，AI 会将其改写成诗，并随机投放到地图某处 |
| 捡起一个瓶子 | 从数据库中随机捞取别人的诗，地图自动定位到该位置 |
| 关闭服务 | 点击窗口底部的「点击此处关闭服务」链接 |

---

## ❓ 常见问题

### 1. 双击 EXE 没反应？
请查看 EXE 同级目录下的 `debug.txt` 文件，里面记录了详细的启动日志和错误信息。

### 2. 为什么提示“未配置 API 密钥”？
您还没有配置 `.env` 文件。请按照“快速开始”中的指引，注册智谱 AI 账号并获取密钥，然后创建 `.env` 文件。

### 3. 智谱 AI 真的免费吗？
是的！`glm-4-flash` 模型**永久免费，不限量**。您只需注册账号即可使用，不会有任何费用。

### 4. 我的密钥安全吗？
**非常安全！** 密钥只保存在您本地的 `.env` 文件中，软件不会上传您的密钥，也不会泄露给任何第三方。您完全可以放心。

### 5. 杀毒软件报毒？
PyInstaller 打包的单文件 EXE 容易被误报。请将其添加到杀毒软件白名单，或使用 `--onedir` 模式重新打包（误报率更低）。

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 本仓库
2. 创建你的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交你的改动 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开一个 Pull Request

---

## 📄 开源协议

本项目采用 [MIT License](LICENSE) 协议，你可以自由使用、修改、商用，只需保留原始版权声明。

---

**愿你在 EchoCast 里，偶遇世界另一端的柔软。** 🌊