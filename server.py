# server.py
from flask import Flask, jsonify
from crawl import get_menu_310
import time

app = Flask(__name__)

@app.route("/")
def index():
    try:
        result = get_menu_310() 
        time.sleep(2) 
        return jsonify({"success": True, "iframe_url": result})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)