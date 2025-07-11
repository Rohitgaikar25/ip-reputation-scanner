# flask_app/app.py
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from abuseipdb import check_ip_reputation
import os


app = Flask(__name__)
CORS(app)  # Enable CORS for external frontend access

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        ip = request.form["ip"]
        result = check_ip_reputation(ip)
    return render_template("index.html", result=result)

@app.route("/api/check-ip", methods=["POST"])
def api_check_ip():
    data = request.get_json()
    ip = data.get("ip")
    result = check_ip_reputation(ip)
    return jsonify(result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)