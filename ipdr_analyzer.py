import pandas as pd
import requests
import time
from tqdm import tqdm

# Replace with your IPInfo API token
API_TOKEN = "API TOKEN HERE"
API_URL = "https://ipinfo.io/{}?token=" + API_TOKEN

# Application mapping based on domain/org keywords
APP_SIGNATURES = {
    
    "Facebook": ["facebook", "fbcdn"],
    "Instagram": ["instagram"],
    "Snapchat": ["snapchat", "scdn"],
    "Twitter / X": ["twitter", "twimg"],
    "LinkedIn": ["linkedin"],
    "Pinterest": ["pinterest"],
    "Reddit": ["reddit"],
    "Discord": ["discord"],
    "WhatsApp": ["whatsapp"],
    "Telegram": ["telegram"],
    "Microsoft Teams": ["teams", "skype", "msedge"],
    "Zoom": ["zoom"],
    "Google Meet": ["meet"],
    "Signal": ["signal"],
    "Messenger": ["messenger"],
    "YouTube": ["youtube", "googlevideo"],
    "Netflix": ["netflix", "nflxvideo"],
    "Amazon Prime Video": ["primevideo", "amazonvideo"],
    "Hotstar / Disney+": ["hotstar", "disneyplus", "disney"],
    "JioCinema": ["jiocinema"],
    "MX Player": ["mxplayer"],
    "Sony LIV": ["sonyliv"],
    "Airtel Xstream": ["airtelxstream"],
    "Twitch": ["twitch"],
    "Spotify": ["spotify"],
    "Wynk Music": ["wynk"],
    "PUBG / BGMI": ["pubg", "bgmi", "battlegroundsmobile"],
    "Free Fire": ["freefire"],
    "Call of Duty Mobile": ["callofduty", "activision"],
    "Clash of Clans": ["clashofclans"],
    "Mobile Premier League (MPL)": ["mpl", "mplgaming"],
    "Dream11": ["dream11"],
    "Amazon": ["amazon"],
    "Flipkart": ["flipkart"],
    "Snapdeal": ["snapdeal"],
    "Myntra": ["myntra"],
    "Meesho": ["meesho"],
    "BigBasket": ["bigbasket"],
    "Blinkit": ["blinkit", "grofers"],
    "Swiggy": ["swiggy"],
    "Zomato": ["zomato"],
    "Uber": ["uber"],
    "Ola": ["olacabs"],
    "IRCTC": ["irctc"],
    "Coursera": ["coursera"],
    "Udemy": ["udemy"],
    "Byju's": ["byjus"],
    "Duolingo": ["duolingo"],
    "Khan Academy": ["khanacademy"],
    "Paytm": ["paytm"],
    "PhonePe": ["phonepe"],
    "Google Pay": ["gpay", "tez", "googlepay"],
    "BHIM": ["bhim"],
    "Razorpay": ["razorpay"],
    "Mobikwik": ["mobikwik"],
    "Gmail": ["gmail", "googlemail"],
    "Yahoo Mail": ["yahoo"],
    "Outlook": ["outlook", "office365"],
    "Google Drive": ["drive.google"],
    "Dropbox": ["dropbox"],
    "Google": ["google"],
    "Truecaller": ["truecaller"],
    "Chrome": ["googlechrome", "gstatic", "chromium"],
    "Edge": ["msedge", "microsoftedge"],
    "Firefox": ["mozilla"],
    "Opera": ["opera"]
}

def identify_application(info):
    host = info.get("hostname", "")
    org = info.get("org", "")
    for app, keywords in APP_SIGNATURES.items():
        if any(keyword.lower() in str(host).lower() or keyword.lower() in str(org).lower() for keyword in keywords):
            return app
    return "Unknown"

def fetch_ip_info(ip):
    try:
        response = requests.get(API_URL.format(ip), timeout=5)
        if response.status_code == 200:
            data = response.json()
            return {
                "IP Address": ip,
                "Hostname": data.get("hostname", "N/A"),
                "Organization": data.get("org", "N/A"),
                "Country": data.get("country", "N/A"),
                "Location": data.get("city", "N/A") + ", " + data.get("region", "N/A"),
                "Is VPN/Proxy/Hosting": "Yes" if data.get("privacy", {}).get("vpn") or data.get("privacy", {}).get("proxy") or data.get("privacy", {}).get("hosting") else "No",
                "Application": identify_application(data)
            }
        else:
            return {"IP Address": ip, "Error": f"HTTP {response.status_code}"}
    except Exception as e:
        return {"IP Address": ip, "Error": str(e)}

def analyze_ipdr_with_api(file_path):
    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        print(f"❌ File '{file_path}' not found.")
        return

    if "Destination IP" not in df.columns:
        print("❌ Excel must contain a 'Destination IP' column.")
        return

    results = []

    for ip in tqdm(df["Destination IP"], desc="Analyzing IPs"):
        ip = str(ip).strip()
        info = fetch_ip_info(ip)
        results.append(info)
        time.sleep(0.6)  # Sleep to avoid rate limits (adjust as needed)

    result_df = pd.DataFrame(results)
    output_file = "ipdr_analysis_with_ipinfo.xlsx"
    result_df.to_excel(output_file, index=False)
    print(f"\n✅ Done. Results saved to '{output_file}'")

# Entry point
if __name__ == "__main__":
    analyze_ipdr_with_api("ipdr_input.xlsx")  # Update filename if needed
