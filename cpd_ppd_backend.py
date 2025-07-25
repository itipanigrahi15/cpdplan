
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

entries = []

@app.route("/entries", methods=["GET"])
def get_entries():
    return jsonify(entries), 200

@app.route("/entries", methods=["POST"])
def add_entry():
    data = request.get_json()
    required_fields = {"type", "performed_by", "count", "status"}
    if not data or not required_fields.issubset(data):
        return jsonify({"error": "Missing required fields"}), 400
    entries.append(data)
    return jsonify({"message": "Entry added successfully"}), 201

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
