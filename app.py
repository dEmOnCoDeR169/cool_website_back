from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)   # allow all origins (safe for hobby projects)

@app.route("/")
def hello():
    return jsonify({"message": "Hello from Flask backend!"})
