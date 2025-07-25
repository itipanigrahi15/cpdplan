from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

entries = []

@app.route('/entries', methods=['GET', 'POST'])
def handle_entries():
    if request.method == 'POST':
        data = request.get_json()
        entries.append(data)
        return jsonify({'message': 'Entry added'}), 201
    return jsonify(entries)

@app.route('/')
def home():
    return "CPD/PPD Backend is running!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
