from flask import Flask,render_template
app=Flask(__name__)
app.config['EXPLAIN_TEMPLATE_LOADING'] = True


@app.route("/")
def index():
    return render_template("index.html") #index