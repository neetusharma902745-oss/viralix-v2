# Viralix 🚀

> **India's #1 Social Media + News + Wikipedia + Google Search Platform**

![Python](https://img.shields.io/badge/Python-3.10+-blue) ![Flask](https://img.shields.io/badge/Flask-3.0-green) ![License](https://img.shields.io/badge/License-MIT-yellow)

---

## ✨ Features

| Page | URL | Description |
|------|-----|-------------|
| 🏠 Feed | `/feed` | Social posts with **real thumbnails**, likes, comments |
| 📰 Articles | `/articles` | Long-form articles with **Wikipedia thumbnails** |
| ✍️ Likho | `/write` | Apna article publish karo |
| 🎬 Video | `/video` | Trending videos with **real preview images** |
| 📢 News | `/news` | Breaking news with **live thumbnails** |
| 🛒 Shopping | `/shop` | Products with discounts + countdown timer |
| 🔍 Google Search | `/google` | **Google-style search** powered by Wikipedia API |
| 📚 Wikipedia | `/wiki` | **Auto Wikipedia article fetch** with images |
| 💬 Messages | `/messages` | Chat list |
| 🔔 Notifications | `/notifications` | Activity feed |
| 👤 Profile | `/profile` | User profile |

---

## 🌟 Special Features

### 🔍 Google-Style Search (`/google`)
- Wikipedia API se real results
- **Featured snippet** with image
- "People Also Ask" section
- Paginated results with thumbnails
- Trending searches
- Ads integrated

### 📚 Wikipedia Auto-Fetch (`/wiki`)
- Koi bhi topic type karo → **Wikipedia se automatic articles fetch**
- Real **thumbnails / images** har article ke saath
- Today's **most-read Wikipedia articles** automatically load
- Live views count

### 🖼 Thumbnails Everywhere
- Feed posts mein real Wikipedia images
- Article cards mein thumbnails
- News cards mein thumbnails
- Video cards mein preview images
- Wiki results mein article images

---

## 🛠 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | **Python 3.10+** / **Flask 3.0** |
| Wikipedia | `urllib` + **Wikipedia REST API** (no extra pip needed) |
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Templates | **Jinja2** |
| Fonts | DM Sans, Syne, Playfair Display |

---

## ⚡ Quick Start

```bash
# 1. Clone karo
git clone https://github.com/YOUR_USERNAME/viralix.git
cd viralix

# 2. Virtual environment
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows

# 3. Install
pip install -r requirements.txt

# 4. Run!
python app.py
```

**Browser mein kholo:**
- 🌐 Main site → http://127.0.0.1:5000
- 🔍 Google Search → http://127.0.0.1:5000/google
- 📚 Wikipedia → http://127.0.0.1:5000/wiki

---

## 📁 Project Structure

```
viralix/
├── app.py                    # Flask app + Wikipedia API + routes
├── requirements.txt          # Dependencies (flask, requests)
├── README.md                 # Yeh file
├── .gitignore
├── templates/
│   ├── index.html            # Main Jinja2 template (sab pages)
│   └── google.html           # Google-style search page
└── static/
    ├── css/
    │   └── style.css         # Dark theme + thumbnail styles
    └── js/
        └── main.js           # Like, post, timer, pills JS
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Home Feed |
| `GET` | `/google?q=query` | Google-style search |
| `GET` | `/wiki?q=query` | Wikipedia auto-fetch |
| `POST` | `/api/post` | Add new post `{content}` |
| `POST` | `/api/like/<id>` | Like a post |
| `GET` | `/api/wiki?q=query` | Wikipedia search JSON |
| `GET` | `/api/wiki/trending` | Today's trending articles JSON |

---

## 📸 Screenshots

> Dark theme • Real Wikipedia thumbnails • Google-style search • Hindi/Hinglish content • Ads integrated

---

## 🚀 Deploy on Railway / Render

```bash
# Procfile banao
echo "web: python app.py" > Procfile

# Push to GitHub, then connect Railway/Render
# Free mein deploy hoga!
```

---

## 📄 License

MIT License — Free to use, modify, distribute.

---

**Made with ❤️ for India 🇮🇳 | Powered by Wikipedia API**
