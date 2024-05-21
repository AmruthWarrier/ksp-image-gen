from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "hello"}), 200

@app.route('/generate_image', methods=['POST'])
def generate_image():
    url = "https://api.limewire.com/api/image/generation"
    prompt = request.json.get('prompt', '')

    payload = {
        "prompt": prompt,
        "aspect_ratio": "1:1"
    }
    headers = {
        "Content-Type": "application/json",
        "X-Api-Version": "v1",
        "Accept": "application/json",
        "Authorization": "Bearer lmwr_sk_29rZYc5LdA_yKwChwUETjnklI63VEcyEEBfbjUZE8eGhPpwk"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return jsonify(data), 200
    else:
        return jsonify({"error": "Failed to generate image"}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)