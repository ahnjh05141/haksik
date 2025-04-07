from flask import Flask, jsonify
import crawl
import json, time

app = Flask(__name__)

@app.route("/lunch", methods=["GET"])
def fetch_lunch():
    try:
        with open("lunch.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify({"success": True, "data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route("/dinner", methods=["GET"])
def fetch_dinner():
    try:
        with open("dinner.json", "r", encoding="utf-8") as f:
            data = json.load(f)
        return jsonify({"success": True, "data": data})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

# ✅ 크론 훅 전용: POST /crawl 들어오면 크롤링해서 menu.json 갱신
@app.route("/crawl", methods=["POST"])
def crawl_hook():
    try:
        lunch = crawl.lunch()
        time.sleep(1)
        dinner = crawl.dinner()
        time.sleep(1)
        with open("lunch.json", "w", encoding="utf-8") as f:
            json.dump({"menus": lunch}, f, ensure_ascii=False, indent=2)
        with open("dinner.json", "w", encoding="utf-8") as f:
            json.dump({"menus": dinner}, f, ensure_ascii=False, indent=2)
        return jsonify({"success": True, "message": "Menu updated"})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)