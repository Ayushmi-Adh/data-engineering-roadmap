import csv
import json
from pathlib import Path

import requests

URL = "https://api.open-meteo.com/v1/forecast"
PARAMS = {
    "latitude": 27.7172,
    "longitude": 85.3240,
    "hourly": "temperature_2m,relative_humidity_2m,precipitation",
    "forecast_days": 3,
    "timezone": "Asia/Kathmandu",
}

RAW_PATH = Path("data/raw/weather_raw.json")
CSV_PATH = Path("data/processed/weather.csv")


def fetch(url, params):
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    return response.json()


def save_json(data, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def to_rows(data):
    h = data["hourly"]
    return [
        {"time": t, "temperature_c": temp, "humidity_pct": hum, "precip_mm": rain}
        for t, temp, hum, rain in zip(
            h["time"], h["temperature_2m"], h["relative_humidity_2m"], h["precipitation"]
        )
    ]


def save_csv(rows, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def main():
    data = fetch(URL, PARAMS)
    save_json(data, RAW_PATH)
    rows = to_rows(data)
    save_csv(rows, CSV_PATH)
    print(f"Saved {len(rows)} rows to {CSV_PATH}")


if __name__ == "__main__":
    main()