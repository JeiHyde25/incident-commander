import argparse
import os
import re

import requests
from dotenv import load_dotenv

load_dotenv()


def get_snow_credentials():
    return (
        os.getenv("SNOW_INSTANCE"),
        os.getenv("SNOW_USER"),
        os.getenv("SNOW_PASS"),
    )


def validate_input(value: str, label: str):
    if not isinstance(value, str):
        raise TypeError(f"{label} must be a string")
    if not value.strip():
        raise ValueError(f"{label} must not be empty")
    if value.strip().isdigit():
        raise ValueError(f"{label} cannot be digits")
    if not re.match(r"^[a-zA-Z0-9\s.,'-]+$", value):
        raise ValueError(f"{label} contains invalid characters.")


def create_incident(short_desc: str, desc: str):
    validate_input(short_desc, "Short Description")
    validate_input(desc, "Description")

    snow_instance, snow_user, snow_pass = get_snow_credentials()
    url = f"{snow_instance}/api/now/table/incident"
    auth = (snow_user, snow_pass)

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
    parser = argparse.ArgumentParser(description="Create a ServiceNow incident.")
    parser.add_argument(
        "--short", required=True, help="Short Description of the incident"
    )
    parser.add_argument(
        "--desc", required=True, help="Full description of the incident"
    )
    args = parser.parse_args()

    try:
        create_incident(args.short, args.desc)
    except (TypeError, ValueError) as e:
        print(f"❌ Input Error: {e}")
        exit(1)
    except Exception as e:
        print(f"❌ Input Error: {e}")
        exit(1)
