from flask import Flask, request, jsonify
from flask_cors import CORS
import hashlib
import requests

app = Flask(__name__)
CORS(app)

@app.route('/api/check-password', methods=['POST'])
def check_password():
    data = request.get_json()
    password = data.get('password', '')

    if not password:
        return jsonify({'error': 'Password required'}), 400

    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]

    try:
        response = requests.get(f'https://api.pwnedpasswords.com/range/{prefix}', timeout=5)
        response.raise_for_status()
    except requests.RequestException:
        return jsonify({'error': 'Failed to reach breach database'}), 500

    breached = False
    count = 0

    for line in response.text.splitlines():
        hash_suffix, occurrences = line.split(':')
        if hash_suffix == suffix:
            breached = True
            count = int(occurrences)
            break

    return jsonify({'breached': breached, 'count': count})


if __name__ == '__main__':
    app.run(debug=True, port=5000)