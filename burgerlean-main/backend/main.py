from flask import Flask,render_template
app=Flask(__name__,template_folder='../frontend/templates')


@app.route("/")
def index():
    return render_template("index.html") #indexhbuj77