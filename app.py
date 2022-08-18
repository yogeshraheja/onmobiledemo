import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Hello everyone we are learning Docker"

@app.route('/thinknyxjenkins')
def hello():
    return "We are trying to build this page using the power of Jenkins"

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)
