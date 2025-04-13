from flask import Flask, jsonify
import crawl, debug
import json

app = Flask(__name__)

# 크론 훅 - POST /crawl 들어오면 크롤링해서 all_daily_menus.json 갱신
@app.route("/crawl", methods=["POST"])
def crawl_hook():
    try:
        crawl.crawl_all_meals()
        return jsonify({"success": True, "message": "Menu updated"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})
    
# 로컬 디버깅 - POST /debug 들어오면 크롤링해서 all_daily_menus.json 갱신
@app.route("/debug", methods=["POST"])
def crawl_locally():
    try:
        debug.crawl_all_meals()
        return jsonify({"success": True, "message": "Menu updated"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})

# 메뉴 api - GET /menus 들어오면 all_daily_menus.json 파일 출력
@app.route("/menus", methods=["GET"])
def fetch_all():
    try:
        with open("all_daily_menus.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify({"success": True, "data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

# 메인 앱 실행
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)