# 🚀 Viralix

<div align="center">

![Viralix Banner](https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/The_Earth_seen_from_Apollo_17.jpg/320px-The_Earth_seen_from_Apollo_17.jpg)

**India's #1 Social Media + News + Wikipedia + Google Search Platform**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Wikipedia](https://img.shields.io/badge/Wikipedia-API-000000?style=for-the-badge&logo=wikipedia&logoColor=white)](https://wikipedia.org)
[![Render](https://img.shields.io/badge/Deployed_on-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)](https://render.com)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

[🌐 Live Demo](https://viralix-v2.onrender.com) · [🐛 Report Bug](https://github.com/neetusharma902745-oss/viralix-v2/issues) · [✨ Request Feature](https://github.com/neetusharma902745-oss/viralix-v2/issues)

</div>

---

## 📋 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Screenshots](#-screenshots)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [Project Structure](#-project-structure)
- [API Endpoints](#-api-endpoints)
- [Deploy](#-deploy)
- [License](#-license)

---

## 🌟 About

**Viralix** ek full-stack web platform hai jo India ke users ke liye banaya gaya hai. Isme social media feed, breaking news, Wikipedia auto-fetch, Google-style search, shopping deals — sab kuch ek jagah available hai.

> *"Ek platform jahan aap post kar sako, news padh sako, Wikipedia se kuch bhi search kar sako, aur shopping bhi kar sako!"*

---

## ✨ Features

### 🏠 Social Feed
- Real-time posts with **Wikipedia thumbnails**
- Like, Comment, Share buttons
- Nayi post likhke instantly publish karo
- Ads integrated naturally

### 📰 Articles
- Long-form articles with **real images**
- Category filter — Tech, Sports, Health, Business
- Apna khud ka article publish karo

### 🔍 Google-Style Search (`/google`)
- Wikipedia API se **real search results**
- Featured snippet with image
- "People Also Ask" section
- Paginated results with thumbnails
- Trending search chips

### 📚 Wikipedia Auto-Fetch (`/wiki`)
- Koi bhi topic likho → **Wikipedia se automatic articles**
- Real thumbnails har article ke saath
- Aaj ke **most-read Wikipedia articles** auto-load
- Live view counts

### 📢 Breaking News
- Live news with color-coded badges
- Real thumbnails
- Breaking, Economy, Sports, Tech categories

### 🛒 Shopping
- Product deals with heavy discounts
- Live countdown sale timer
- Cart functionality

### 💬 Messages & Notifications
- Chat list with online status
- Real-time notification feed

---

## 📸 Screenshots

| Feed | Google Search | Wikipedia |
|------|--------------|-----------|
| Social posts with thumbnails | Real Wikipedia results | Auto-fetched articles |

| News | Shopping | Articles |
|------|---------|---------|
| Breaking news live | Products with deals | Long-form content |

---

## 🛠 Tech Stack

| Layer | Technology | Version |
|-------|-----------|---------|
| **Backend** | Python + Flask | 3.10+ / 3.0 |
| **Wikipedia** | Wikipedia REST API | Free (no key needed) |
| **Server** | Gunicorn | 21.2+ |
| **Frontend** | HTML5 + CSS3 + Vanilla JS | — |
| **Templates** | Jinja2 | Built-in Flask |
| **Fonts** | Google Fonts | DM Sans, Syne, Playfair |
| **Deploy** | Render | Free Tier |

---

## 🚀 Getting Started

### Prerequisites
```bash
Python 3.10+
pip
git
```

### Installation

```bash
# 1. Clone karo
git clone https://github.com/neetusharma902745-oss/viralix-v2.git
cd viralix-v2

# 2. Virtual environment banao
python -m venv venv

# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate

# 3. Dependencies install karo
pip install -r requirements.txt

# 4. Server chalao
python app.py
```

### Browser mein kholo
```
🌐 Main Site     →  http://127.0.0.1:5000
🔍 Google Search →  http://127.0.0.1:5000/google
📚 Wikipedia     →  http://127.0.0.1:5000/wiki
```

---

## 📁 Project Structure

```
viralix-v2/
│
├── 📄 app.py                    # Flask main app + Wikipedia API + all routes
├── 📄 requirements.txt          # Python dependencies
├── 📄 README.md                 # Yeh file
├── 📄 .gitignore
│
├── 📁 templates/
│   ├── 📄 index.html            # Main Jinja2 template (sab pages)
│   └── 📄 google.html           # Google-style search page
│
└── 📁 static/
    ├── 📁 css/
    │   └── 📄 style.css         # Dark theme + all component styles
    └── 📁 js/
        └── 📄 main.js           # Like, post, timer, search JS
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description | Response |
|--------|----------|-------------|----------|
| `GET` | `/` | Home Feed | HTML |
| `GET` | `/feed` | Social Feed | HTML |
| `GET` | `/articles` | Articles List | HTML |
| `POST` | `/write` | Publish Article | HTML |
| `GET` | `/video` | Video Page | HTML |
| `GET` | `/news` | Breaking News | HTML |
| `GET` | `/shop` | Shopping Page | HTML |
| `GET` | `/wiki?q=query` | Wikipedia Search | HTML |
| `GET` | `/google?q=query` | Google Search | HTML |
| `GET` | `/messages` | Messages | HTML |
| `GET` | `/notifications` | Notifications | HTML |
| `GET` | `/profile` | User Profile | HTML |
| `POST` | `/api/post` | Add New Post | `{"ok": true, "post": {...}}` |
| `POST` | `/api/like/<id>` | Like a Post | `{"ok": true, "likes": 100}` |
| `GET` | `/api/wiki?q=query` | Wiki Search JSON | `[{title, excerpt, thumbnail, url}]` |
| `GET` | `/api/wiki/trending` | Trending Articles | `[{title, excerpt, views}]` |

---

## ☁️ Deploy

### Render par Deploy karo (Free)

```bash
# 1. GitHub par push karo
git add .
git commit -m "Deploy Viralix"
git push origin main

# 2. render.com par jao
# New Web Service → GitHub repo connect karo

# 3. Settings:
#    Build Command:  pip install -r requirements.txt
#    Start Command:  gunicorn app:app --bind 0.0.0.0:$PORT
#    Environment:    Python 3

# 4. Deploy! ✅
```

### Railway par Deploy karo

```bash
# railway.app → New Project → Deploy from GitHub
# Start Command: gunicorn app:app --bind 0.0.0.0:$PORT
```

---

## 🤝 Contributing

1. Fork karo
2. Feature branch banao (`git checkout -b feature/AmazingFeature`)
3. Commit karo (`git commit -m 'Add AmazingFeature'`)
4. Push karo (`git push origin feature/AmazingFeature`)
5. Pull Request kholo

---

## 📄 License

MIT License — Free to use, modify, and distribute.

```
Copyright (c) 2026 Viralix
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software...
```

---

## 👨‍💻 Author

**Neetu Sharma**
- GitHub: [@neetusharma902745-oss](https://github.com/neetusharma902745-oss)

---

<div align="center">

**Made with ❤️ for India 🇮🇳**

*Powered by Wikipedia API • Deployed on Render • Built with Flask*

⭐ **Agar pasand aaya toh Star dena mat bhoolna!** ⭐

</div>
