# flask_app/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from abuseipdb import check_ip_reputation

app = Flask(__name__)
CORS(app)  # Enable CORS for external frontend access

@app.route("/api/check-ip", methods=["POST"])
def api_check_ip():
    data = request.get_json()
    ip = data.get("ip")
    result = check_ip_reputation(ip)
    return jsonify(result)
