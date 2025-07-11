# flask_app/app.py
from flask import Flask, render_template, request
from abuseipdb import check_ip_reputation

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        ip = request.form["ip"]
        result = check_ip_reputation(ip)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
