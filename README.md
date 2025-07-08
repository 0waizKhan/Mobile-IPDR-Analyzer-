# 📡 Mobile-IPDR-Analyzer

A Python-based automation tool to analyze Mobile IPDR (Internet Protocol Detail Records) for investigative or operational purposes. The tool enriches IPDR data with external threat intelligence and identifies application usage patterns, VPN activity, suspicious domains, and geo-locations.

---

## 🚀 Features

- 📄 Read and parse Excel-based IPDR files
- 🌐 Enrich IPs using **IPInfo API**
- 🧠 Application and domain categorization using keyword mapping
- 🕵️ VPN/proxy detection logic
- 📍 GeoIP tagging (Country, City, Org)
- 📊 Summary metrics for investigations

---

## 🛠️ Technologies Used

- Python 3.x
- Pandas
- Requests
- tqdm (progress bar)
- IPInfo API (for IP enrichment)

---

## 📦 Installation

1. **Clone the repository**

2. Install dependencies: pip install -r requirements.txt

3. Set your IPInfo API Token: API_TOKEN = "your_ipinfo_token_here"

How to Use

1. Place your IPDR Excel file in the root directory (e.g., ipdr_input.xlsx)

Run the script: python ipdr_analyzer.py

🔐 VPN Detection Logic

Detects IPs associated with hosting providers or anonymizers

Flags unknown domains with unrecognized keywords

Checks for mismatched org/country patterns

👨‍💻 Author
Owaiz Khan
Security Researcher | Automation Enthusiast
