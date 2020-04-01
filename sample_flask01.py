from flask import Flask,render_template

app= Flask(__name__)

@app.route("/")
def index():
    headline="Hello World"
    return render_template("C:/Users/Chirag/Desktop/Flask_chirag/index.html",headline=headline)


@app.route("/<string:name>")
def hello(name):
        name=name.capitalize()
        return f"Hello, {name}!"