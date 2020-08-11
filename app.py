# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)


# A welcome message to test our server
def index():
    return "<h1>You are beautiful</h1>"

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
