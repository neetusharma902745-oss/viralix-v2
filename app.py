"""
Viralix — India's #1 Social + News + Wiki Platform
Flask backend with Wikipedia auto-fetch, thumbnails, ads
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for
from datetime import datetime
import json, urllib.parse, urllib.request, html

app = Flask(__name__)

# ─────────────────────────────────────────────
#  Wikipedia API helper  (no pip package needed)
# ─────────────────────────────────────────────

WIKI_API = "https://en.wikipedia.org/w/api.php"

def wiki_search(query, limit=6):
    """Search Wikipedia and return list of {title, excerpt, thumbnail, url}"""
    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "srlimit": limit,
        "format": "json",
        "utf8": 1,
    }
    url = WIKI_API + "?" + urllib.parse.urlencode(params)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Viralix/1.0"})
        with urllib.request.urlopen(req, timeout=5) as r:
            data = json.loads(r.read())
        results = []
        for item in data.get("query", {}).get("search", []):
            title = item["title"]
            snippet = html.unescape(item.get("snippet", "")).replace('<span class="searchmatch">', "").replace("</span>", "")
            results.append({
                "title": title,
                "excerpt": snippet[:200] + "...",
                "url": f"https://en.wikipedia.org/wiki/{urllib.parse.quote(title)}",
                "thumbnail": get_wiki_thumbnail(title),
            })
        return results
    except Exception:
        return []

def get_wiki_thumbnail(title):
    """Fetch thumbnail URL for a Wikipedia article"""
    params = {
        "action": "query",
        "titles": title,
        "prop": "pageimages",
        "pithumbsize": 300,
        "format": "json",
        "utf8": 1,
    }
    url = WIKI_API + "?" + urllib.parse.urlencode(params)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Viralix/1.0"})
        with urllib.request.urlopen(req, timeout=4) as r:
            data = json.loads(r.read())
        pages = data.get("query", {}).get("pages", {})
        for page in pages.values():
            thumb = page.get("thumbnail", {}).get("source")
            if thumb:
                return thumb
    except Exception:
        pass
    return None

def wiki_trending():
    """Fetch today's featured article from Wikipedia"""
    today = datetime.utcnow()
    url = (
        f"https://en.wikipedia.org/api/rest_v1/feed/featured/"
        f"{today.year}/{today.month:02d}/{today.day:02d}"
    )
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Viralix/1.0"})
        with urllib.request.urlopen(req, timeout=6) as r:
            data = json.loads(r.read())
        articles = []
        # Most read articles
        for item in data.get("mostread", {}).get("articles", [])[:8]:
            articles.append({
                "title": item.get("title", "").replace("_", " "),
                "excerpt": item.get("extract", "")[:180] + "...",
                "url": item.get("content_urls", {}).get("desktop", {}).get("page", "#"),
                "thumbnail": (item.get("thumbnail") or item.get("originalimage") or {}).get("source"),
                "views": f"{item.get('views', 0):,}",
            })
        return articles
    except Exception:
        return []

# ─────────────────────────────────────────────
#  Static data
# ─────────────────────────────────────────────

THUMBNAILS = [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Left_side_of_flying_airplane.jpg/320px-Left_side_of_flying_airplane.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Biryani_Home_Cooked.jpg/320px-Biryani_Home_Cooked.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1e/Sunrise_over_the_sea.jpg/320px-Sunrise_over_the_sea.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/320px-Image_created_with_a_mobile_phone.png",
    "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Camponotus_flavomarginatus_ant.jpg/320px-Camponotus_flavomarginatus_ant.jpg",
]

EMOJI_THUMBS = {
    "tech":    "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/320px-Python-logo-notext.svg.png",
    "cricket": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/86/Cricket_ball_old.jpg/320px-Cricket_ball_old.jpg",
    "food":    "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Biryani_Home_Cooked.jpg/320px-Biryani_Home_Cooked.jpg",
    "space":   "https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/The_Earth_seen_from_Apollo_17.jpg/320px-The_Earth_seen_from_Apollo_17.jpg",
    "music":   "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Guitar_chords.jpg/320px-Guitar_chords.jpg",
    "money":   "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Indian_500_rupee_note_%28obverse%29.jpg/320px-Indian_500_rupee_note_%28obverse%29.jpg",
}

posts = [
    {
        "id": 1, "author": "Rahul Sharma", "avatar": "🧑",
        "location": "Delhi", "time": "5 min pehle",
        "content": "India ne aaj ek naya AI record toda! Ab hum duniya mein 3rd position par hain. #IndiaAI #TechIndia",
        "likes": 2400, "comments": 318, "shares": 89,
        "thumbnail": EMOJI_THUMBS["tech"],
        "img_label": "AI Summit 2026, Bangalore",
    },
    {
        "id": 2, "author": "Priya Singh", "avatar": "👩",
        "location": "Mumbai", "time": "22 min pehle",
        "content": "Marine Drive ka ye sunset — ekdum magical tha! Mumbai zindaabad 🌆 #Mumbai #Sunset",
        "likes": 5100, "comments": 421, "shares": 212,
        "thumbnail": EMOJI_THUMBS["space"],
        "img_label": "Marine Drive, Mumbai",
    },
    {
        "id": 3, "author": "Cricket Guru", "avatar": "🏏",
        "location": "Trending", "time": "1 ghanta pehle",
        "content": "India ne ICC T20 World Cup jeeta! Rohit Sharma ka shandar performance. #Cricket #TeamIndia",
        "likes": 18200, "comments": 2100, "shares": 4800,
        "thumbnail": EMOJI_THUMBS["cricket"],
        "img_label": "ICC T20 World Cup 2026",
    },
    {
        "id": 4, "author": "Food Lover", "avatar": "🍛",
        "location": "Lucknow", "time": "2 ghante pehle",
        "content": "Lucknawi Biryani ki recipe share kar raha hoon — ghar par banao restaurant jaisi! #Food #Recipe",
        "likes": 7600, "comments": 943, "shares": 1200,
        "thumbnail": EMOJI_THUMBS["food"],
        "img_label": "Lucknawi Dum Biryani",
    },
]

articles = [
    {
        "id": 1, "title": "AI ka Bhavishya: 2030 tak kya badlega?",
        "excerpt": "Artificial Intelligence sirf ek technology nahi — yeh ek revolution hai. 2030 tak AI doctors se behtar diagnose karega...",
        "author": "Rohit Kumar", "initials": "RK", "date": "14 March 2026",
        "reads": "12.3K", "read_time": "8 min", "category": "Technology",
        "thumbnail": EMOJI_THUMBS["tech"], "bg": "#0a0a20",
    },
    {
        "id": 2, "title": "IPL 2026 — Kaunsi Team Trophy Uthayegi?",
        "excerpt": "Is saal IPL mein competition bahut tough hai. Har team ne naye players liye hain...",
        "author": "Cricket Guru", "initials": "CG", "date": "13 March 2026",
        "reads": "9.8K", "read_time": "5 min", "category": "Sports",
        "thumbnail": EMOJI_THUMBS["cricket"], "bg": "#1a0808",
    },
    {
        "id": 3, "title": "Ghar Baithe Paise Kamao — 10 Tarike",
        "excerpt": "Internet ne aaj har ghar mein paise kamane ke mauqe de diye hain...",
        "author": "FinanceGuru", "initials": "FG", "date": "12 March 2026",
        "reads": "24.1K", "read_time": "7 min", "category": "Business",
        "thumbnail": EMOJI_THUMBS["money"], "bg": "#081a08",
    },
    {
        "id": 4, "title": "ISRO Chandrayaan-4 — India ka Moon Mission",
        "excerpt": "ISRO ne ek baar phir itihaas rachha! Chandrayaan-4 safaltapurvak launch hua...",
        "author": "Space India", "initials": "SI", "date": "11 March 2026",
        "reads": "31.5K", "read_time": "6 min", "category": "Science",
        "thumbnail": EMOJI_THUMBS["space"], "bg": "#080820",
    },
]

news_items = [
    {"emoji": "🚀", "badge": "Breaking", "btype": "r",
     "title": "ISRO ka Chandrayaan-4 moon par safely utaraa — India ne rachha naya itihaas!",
     "source": "ISRO", "time": "8 min pehle",
     "thumbnail": EMOJI_THUMBS["space"]},
    {"emoji": "💰", "badge": "Economy",  "btype": "b",
     "title": "Sensex pehli baar 1 lakh ke paar — share market mein investors ka josh",
     "source": "ET Markets", "time": "34 min pehle",
     "thumbnail": EMOJI_THUMBS["money"]},
    {"emoji": "🏏", "badge": "Sports",   "btype": "g",
     "title": "India ne ICC T20 World Cup 2026 jeeta! Rohit Sharma Man of Tournament",
     "source": "Cricinfo", "time": "1 ghanta pehle",
     "thumbnail": EMOJI_THUMBS["cricket"]},
    {"emoji": "🤖", "badge": "Tech",     "btype": "b",
     "title": "OpenAI ka GPT-6 launch — ek hi prompt mein 10 ghante ka kaam",
     "source": "TechCrunch", "time": "2 ghante pehle",
     "thumbnail": EMOJI_THUMBS["tech"]},
    {"emoji": "🍛", "badge": "Lifestyle","btype": "g",
     "title": "Lucknow ki biryani UNESCO heritage list mein shamil — India ka garv",
     "source": "Times of India", "time": "3 ghante pehle",
     "thumbnail": EMOJI_THUMBS["food"]},
]

products = [
    {"emoji": "📱", "name": "Smartphone Pro 2026",    "stars": 5, "price": "₹24,999", "old": "₹45,000", "disc": "44%",
     "thumbnail": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/120px-Image_created_with_a_mobile_phone.png"},
    {"emoji": "💻", "name": "Gaming Laptop Ultra",    "stars": 4, "price": "₹69,999", "old": "₹99,999", "disc": "30%", "thumbnail": None},
    {"emoji": "🎧", "name": "Noise-Cancel Headphones","stars": 5, "price": "₹4,499",  "old": "₹8,999",  "disc": "50%", "thumbnail": None},
    {"emoji": "⌚", "name": "Smart Watch Series 8",   "stars": 4, "price": "₹12,999", "old": "₹19,999", "disc": "35%", "thumbnail": None},
    {"emoji": "📷", "name": "DSLR Camera Kit",        "stars": 5, "price": "₹38,999", "old": "₹55,000", "disc": "29%", "thumbnail": None},
    {"emoji": "🖥",  "name": '4K Monitor 32"',         "stars": 4, "price": "₹22,499", "old": "₹34,999", "disc": "36%", "thumbnail": None},
]

# ─────────────────────────────────────────────
#  Routes
# ─────────────────────────────────────────────

@app.route("/")
@app.route("/feed")
def feed():
    return render_template("index.html", posts=posts, page="feed")

@app.route("/articles")
def articles_page():
    return render_template("index.html", articles=articles, page="article")

@app.route("/write", methods=["GET", "POST"])
def write():
    success, pub_title = False, ""
    if request.method == "POST":
        title    = request.form.get("title", "").strip()
        content  = request.form.get("content", "").strip()
        category = request.form.get("category", "General")
        if title and len(content) >= 10:
            articles.insert(0, {
                "id": len(articles) + 1,
                "title": title,
                "excerpt": content[:160] + "..." if len(content) > 160 else content,
                "author": "Aap (You)", "initials": "AP",
                "date": datetime.now().strftime("%d %B %Y"),
                "reads": "0", "read_time": f"{max(1, len(content)//500)} min",
                "category": category,
                "thumbnail": None, "bg": "#1a1a2e",
            })
            success, pub_title = True, title
    return render_template("index.html", page="write", success=success, pub_title=pub_title)

@app.route("/video")
def video():
    return render_template("index.html", page="video")

@app.route("/news")
def news_page():
    return render_template("index.html", news=news_items, page="news")

@app.route("/shop")
def shop():
    return render_template("index.html", products=products, page="shop")

@app.route("/messages")
def messages():
    return render_template("index.html", page="msg")

@app.route("/notifications")
def notifications():
    return render_template("index.html", page="notif")

@app.route("/profile")
def profile():
    return render_template("index.html", articles=articles[:4], page="profile")

@app.route("/wiki")
def wiki():
    query   = request.args.get("q", "").strip()
    results = wiki_search(query) if query else []
    trending = wiki_trending()
    return render_template("index.html", page="wiki",
                           wiki_query=query,
                           wiki_results=results,
                           wiki_trending=trending)

@app.route("/google")
def google_page():
    query   = request.args.get("q", "").strip()
    results = wiki_search(query, limit=8) if query else []
    return render_template("google.html", query=query, results=results)

# ─────────────────────────────────────────────
#  API
# ─────────────────────────────────────────────

@app.route("/api/post", methods=["POST"])
def api_add_post():
    data    = request.get_json(silent=True) or {}
    content = data.get("content", "").strip()
    if not content:
        return jsonify({"ok": False, "error": "Content required"}), 400
    new_post = {
        "id": len(posts) + 1,
        "author": "Aap (You)", "avatar": "😊",
        "location": "Meerut, UP", "time": "Abhi",
        "content": content,
        "likes": 0, "comments": 0, "shares": 0,
        "thumbnail": None, "img_label": None,
    }
    posts.insert(0, new_post)
    return jsonify({"ok": True, "post": new_post})

@app.route("/api/like/<int:pid>", methods=["POST"])
def api_like(pid):
    post = next((p for p in posts if p["id"] == pid), None)
    if not post:
        return jsonify({"ok": False}), 404
    post["likes"] += 1
    return jsonify({"ok": True, "likes": post["likes"]})

@app.route("/api/wiki")
def api_wiki():
    q = request.args.get("q", "").strip()
    if not q:
        return jsonify([])
    return jsonify(wiki_search(q, limit=6))

@app.route("/api/wiki/trending")
def api_wiki_trending():
    return jsonify(wiki_trending())

if __name__ == "__main__":
    print("\n" + "="*55)
    print("  🚀  Viralix Server Start Ho Raha Hai!")
    print("  🌐  http://127.0.0.1:5000        — Main Site")
    print("  🔍  http://127.0.0.1:5000/google — Google-style Search")
    print("  📚  http://127.0.0.1:5000/wiki   — Wikipedia Auto-fetch")
    print("="*55 + "\n")
    app.run(debug=True, port=5000)
