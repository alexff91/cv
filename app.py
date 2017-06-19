from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/nikita")
def helloNikita():
    return "Hello Nikita!"
