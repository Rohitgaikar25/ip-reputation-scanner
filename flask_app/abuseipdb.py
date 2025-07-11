# flask_app/abuseipdb.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("ABUSEIPDB_API_KEY")

def check_ip_reputation(ip):
    url = "https://api.abuseipdb.com/api/v2/check"
    headers = {
        'Key': API_KEY,
        'Accept': 'application/json'
    }
    params = {
        'ipAddress': ip,
        'maxAgeInDays': 90
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()
