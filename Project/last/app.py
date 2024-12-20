from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

@app.route('/last', methods=['GET'])
def get_last():
    try:
        with open('last.json', 'r') as f:
            data = json.load(f)
        return jsonify(data), 200
    except FileNotFoundError:
        return 'No operations yet', 404

@app.route('/notify', methods=['POST'])
def save_last():
    data = request.get_json()
    if data:
        with open('last.json', 'w') as f:
            json.dump(data, f)
        return 'Saved', 200
    return 'Invalid data', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
