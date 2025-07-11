# cli_scanner.py
from flask_app.abuseipdb import check_ip_reputation

def main():
    ip = input("Enter IP address to check: ").strip()
    result = check_ip_reputation(ip)
    if 'data' in result:
        data = result['data']
        print(f"\nIP: {data['ipAddress']}")
        print(f"Country: {data.get('countryCode')}")
        print(f"Abuse Confidence Score: {data['abuseConfidenceScore']}")
        print(f"Total Reports: {data['totalReports']}")
        print(f"Last Reported At: {data['lastReportedAt']}")
    else:
        print("Error:", result.get('errors', result))

if __name__ == "__main__":
    main()
