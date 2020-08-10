from flask import Flask
app = flask.Flask(__name__)

@app.route("/")
def index():
    #do whatevr here...
    return "Hello Hero_Basic_ko!"
