from flask import Flask, jsonify
import requests, os

app = Flask(__name__)
INVENTORY_URL = os.environ.get("INVENTORY_URL", "http://inventory:1337/inventory")
SENSOR_PORT   = os.environ.get("SENSOR_PORT", "9100")

@app.get("/sd")
def sd():
    try:
        names = requests.get(INVENTORY_URL, timeout=3).json() or []
    except Exception:
        names = []
    targets = [f"{name}:{SENSOR_PORT}" for name in names]
    return jsonify([{"targets": targets, "labels": {"job": "sensor"}}])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)
