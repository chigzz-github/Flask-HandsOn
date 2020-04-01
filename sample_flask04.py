from flask import Flask,render_template

app= Flask(__name__)

@app.route("/<name>")
def name():
    return render_template("templates/index.html",info=name)
    
    
if __name__=="__main__":
    app.run()