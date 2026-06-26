# 🌊 EchoCast · Echo Drift

> Not social media, but serendipity. Be the one who throws a bottle into the cyber sea.

[![GitHub stars](https://img.shields.io/github/stars/20140804/EchoCast)](https://github.com/20140804/EchoCast/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/20140804/EchoCast)](https://github.com/20140804/EchoCast/network)
[![GitHub license](https://img.shields.io/github/license/20140804/EchoCast)](https://github.com/20140804/EchoCast/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)

---

## 📖 Introduction

**EchoCast** is a lightweight, anonymous poetic message-in-a-bottle app. You simply write down a passing thought, and AI (powered by Zhipu GLM-4-Flash) transforms it into a short poem, then tosses it to a random latitude/longitude coordinate on the globe. Another stranger, somewhere else, can randomly pick up your anonymous message and see it appear on a world map.

**This world has enough productivity tools; what it lacks is unexpected romance.**

---

## ✨ Core Features

- 🗺️ **Geolocated messages**: Every letter is pinned to a real-world coordinate on the map.
- 🤖 **AI-powered poetry**: Uses Zhipu AI's free `glm-4-flash` model to turn plain text into poetic verse (**permanently free**).
- 🎭 **Fully anonymous**: No sign-up, no login, no trace. Only pure words and chance encounters.
- 📦 **Ready to run**: Packaged as a standalone EXE desktop application – double-click to launch, no Python installation required.

---

## 🆓 Free vs Pro

| Feature | Free | Pro |
|---------|------|-----|
| AI Poetry (Chinese) | ✅ | ✅ |
| AI Poetry (English) | ❌ | ✅ |
| 4 Poetry Styles | ❌ (Default only) | ✅ |
| One-Click Copy | ❌ | ✅ |
| Export as PNG | ❌ | ✅ |
| My History | ❌ | ✅ |
| License Key Activation | ❌ | ✅ |

**Pro Version: 9.9 RMB (~$1.99 USD) — Lifetime License**

---

## 🔑 How to Get Pro

1. Download the free version from [Releases](https://github.com/20140804/EchoCast/releases)
2. Contact the developer to purchase a Pro license:
   - **WeChat:** [GreatFrostPiercePro]
   - **Email:** [EchoCast_BuyPro@hotmail.com]
   - **Platform:** 爱发电 / 闲鱼 (search "EchoCast")
3. After payment, you will receive a `license.key` file
4. Place `license.key` in the same folder as `EchoCast.exe`
5. Restart the software — Pro features unlock automatically! 🚀

---

## 🚀 Quick Start

### Step 1: Download the Software

Go to the [Releases](https://github.com/20140804/EchoCast/releases) page and download `EchoCast.exe`.

### Step 2: Get Your Free API Key (Critical Step)

EchoCast uses Zhipu AI's `glm-4-flash` model, which is **permanently free**. You only need to spend 2 minutes signing up and getting a key.

1. Visit [Zhipu AI Open Platform](https://open.bigmodel.cn/) and register an account.
2. After logging in, go to **Console** → **API Keys**.
3. Click **Create New API Key** and copy the generated key (format: `sk-xxxxxx`).

### Step 3: Configure the Key

1. Place `EchoCast.exe` in a separate folder.
2. In the **same folder**, create a file named `.env` (note the leading dot).
3. Open `.env` with Notepad and write the following:
ZHIPU_API_KEY=your-api-key-here
Replace `your-api-key-here` with the actual key you just copied.

### Step 4: Run

Double-click `EchoCast.exe` and the software will open automatically. On first run, it will detect the key – if not configured, a guided popup will help you complete the setup.

---

## 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Backend | Python 3.8+ / Flask |
| AI API | Zhipu AI (GLM-4-Flash) via OpenAI-compatible SDK |
| Frontend Map | Leaflet.js + OpenStreetMap |
| Desktop Framework | PyQt5 + QWebEngineView |
| Database | SQLite (zero-config, single file) |
| Packaging | PyInstaller (generates standalone EXE) |

---

## 🧭 How to Use

| Action | Description |
|--------|-------------|
| Write your thought → Throw into the sea | Enter text – AI will turn it into a poem and drop it at a random location on the map |
| Pick up a bottle | Randomly fetch someone else's poem from the database – the map will zoom to its location |
| Shut down the server | Click the "Click here to shutdown" link at the bottom of the window |

### Pro Only: Language & Style

- **Language:** Choose Chinese or English for AI poetry
- **Style:** 4 styles — Default / Classical Chinese / Modern / Haiku
- **Copy:** One-click copy any poem
- **Export:** Save poetry as PNG image
- **History:** View all your thrown bottles

---

## ❓ FAQ

### 1. Nothing happens when I double-click the EXE?
Check the `debug.txt` file in the same directory – it logs all startup details and error messages.

### 2. Why does it say "API key not configured"?
You haven't set up the `.env` file yet. Follow the "Quick Start" guide to register for a Zhipu AI account, get a key, and create the `.env` file.

### 3. Is Zhipu AI really free?
Yes! The `glm-4-flash` model is **permanently free and unlimited**. You just need to register an account – no charges will ever apply.

### 4. Is my key secure?
**Very secure!** The key is stored only in your local `.env` file. The software never uploads your key or leaks it to any third party. You can rest assured.

### 5. Antivirus flags the EXE as suspicious?
PyInstaller single-file EXEs are often falsely flagged. Please add it to your antivirus whitelist, or repackage using the `--onedir` mode (which has a lower false-positive rate).

### 6. How do I activate Pro?
Place the `license.key` file in the same folder as `EchoCast.exe` and restart the software. Pro features will unlock automatically.

---

## 💰 Pro Version Purchase

| Region | Price | Payment Methods |
|--------|-------|-----------------|
| China | 9.9 RMB | WeChat / Alipay / 爱发电 / 闲鱼 |
| Global | ~$1.99 USD | Coming soon (PayPal) |

**Contact to purchase:**
- **WeChat:** [GreatFrostPiercePro]
- **Email:** [EchoCast_BuyPro@hotmail.com]
- **GitHub Issues:** https://github.com/20140804/EchoCast/issues

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork this repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE) – you are free to use, modify, and distribute it commercially, as long as you retain the original copyright notice.

---
## If you want to talk with me about the features, Welcome!! 
Offical Email: EchoCast_Official@outlook.com
## If you want to Buy Pro version, please send an email to this
Buy Pro Version Email:EchoCast_BuyPro@outlook.com

---

**May you encounter the softness from the other side of the world in EchoCast.** 🌊
