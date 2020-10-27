from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/competidores")
def competidor():
    return render_template("competidores.html")

app.run()
