from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app=Flask(__name__,template_folder='../frontend/templates')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate=Migrate(app,db)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/my_burgerlean'

class burger(db.Model):
    __tablename__='burger'
    burgerID = db.Column(db.Integer, primary_key=True)
    burgerName=db.Column(db.String(20),nullable=False)
    burgerPrice=db.Column(db.Integer,nullable=False)

class log(db.Model):
    __tablename__="log"
    logID=db.Column(db.Integer,primary_key=True)
    date=db.Column(db.Date,nullable=False)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/prodotti.html")
def prodotti():
    return render_template("prodotti.html")

@app.route("/contattaci.html")
def contattaci():
    return render_template("contattaci.html")

@app.route("/crediti.html")
def crediti():
    return render_template("crediti.html")


