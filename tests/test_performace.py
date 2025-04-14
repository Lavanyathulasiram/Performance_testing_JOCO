import sys
import os
import time
from datetime import datetime, timedelta
import requests

# Step 1: Add project root to Python path
sys.path.append("D:\\JOCO_API")  # Update this path if your project is somewhere else

# Step 2: Corrected import from config/config.py
from config import config

# Step 3: Other imports from your framework
from payloads.search_payload import build_rest_payload, build_ws_payload
from utils.ws_handler import run_ws

# Result container
results = []

# Test Dates: 70 days from May 7, 2025
start_date = datetime(2025, 5, 7, 18, 30)
date_list = [start_date + timedelta(days=i) for i in range(5)]

# Main Test Loop
for date in date_list:
    print(f"\n🔄 Testing: {date.strftime('%Y-%m-%d')}")
    rest_payload = build_rest_payload(date)
    start_time = time.time()

    try:
        response = requests.post(config.API_URL, json=rest_payload, headers=config.rest_headers)
        key = response.text.strip()
        print(f"🔑 Extracted Key: {key}")
    except Exception as e:
        print(f"❌ REST Error: {e}")
        continue

    result_container = {
        "Travel Date": date.strftime("%Y-%m-%d"),
        "Start Time": datetime.fromtimestamp(start_time).strftime("%Y-%m-%d %H:%M:%S"),
        "End Time": "",
        "Response Time (ms)": "",
        "Status Code": response.status_code,
        "Response": key,
        "Status": "",
        "Message": ""
    }

    ws_payload = build_ws_payload(key, rest_payload, config.JWT_TOKEN, config.X_AUTH_TOKEN)
    run_ws(config.WSS_URL, config.ws_headers, ws_payload, result_container, results, start_time, config.EXCEL_FILE)
