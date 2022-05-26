from flask import flask, render_template
app=flask(__name__)

@app.route("/")
def index():
    render_template("index.html") #index