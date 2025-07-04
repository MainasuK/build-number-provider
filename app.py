import os
from flask import Flask, request, jsonify
import json

app = Flask(__name__)
BUILD_NUMBER_FILE = 'build_number.txt'


def get_saved_build_number():
    if os.path.exists(BUILD_NUMBER_FILE):
        with open(BUILD_NUMBER_FILE, 'r') as f:
            try:
                return int(f.read().strip())
            except Exception:
                return 0
    return 0


def save_build_number(number):
    with open(BUILD_NUMBER_FILE, 'w') as f:
        f.write(str(number))


@app.route('/v1/build_number', methods=['POST'])
def build_number():
    content = request.get_json()
    latest_build_number = content.get("latest_build_number")
    if latest_build_number is None or not isinstance(latest_build_number, int):
        return jsonify({"error": "latest_build_number must be provided as an integer"}), 400
    saved_build_number = get_saved_build_number()
    largest = max(saved_build_number, latest_build_number)
    next_build_number = largest + 1
    save_build_number(next_build_number)
    return jsonify({"next_build_number": next_build_number})
