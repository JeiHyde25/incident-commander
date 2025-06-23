import os
from dotenv import load_dotenv
import requests

load_dotenv()

SNOW_INSTANCE = os.getenv("SNOW_INSTANCE")
SNOW_USER = os.getenv("SNOW_USER")
SNOW_PASS = os.getenv("SNOW_PASS")
def create_incident(short_desc: str, desc: str):
    url = f"{SNOW_INSTANCE}/api/now/table/incident"
    auth = (SNOW_USER, SNOW_PASS)

    payload = {
        "short_description": short_desc,
        "description": desc,
        "urgency": "2",
        "impact": "2",
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

    response = requests.post(url, auth=auth, json=payload, headers=headers)

    if response.status_code == 201:
        print("✅ Incident created:", response.json()["result"]["number"])
    else:
        print("❌ Failed:", response.status_code, response.text)
if __name__ == "__main__":
    create_incident(
        "Test incident", "This is a test from the Incident Commander script."
    )
