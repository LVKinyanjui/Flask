from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return {"message": "Hello World"}
    return jsonify(message="hello My world")
    