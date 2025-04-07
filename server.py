from flask import Flask, jsonify
from crawl import get_menu_310
import json, time

app = Flask(__name__)

# ✅ 메인 화면: 저장된 menu.json 파일 읽어서 보여주기
@app.route("/", methods=["GET"])
def index():
    try:
        with open("menu.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify({"success": True, "data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

# ✅ 크론 훅 전용: POST /crawl 들어오면 크롤링해서 menu.json 갱신
@app.route("/crawl", methods=["POST"])
def crawl_hook():
    try:
        menus = get_menu_310()
        time.sleep(2)
        with open("menu.json", "w", encoding="utf-8") as f:
            json.dump({"menus": menus}, f, ensure_ascii=False, indent=2)
        return jsonify({"success": True, "message": "Menu updated"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)