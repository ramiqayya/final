from flask import Flask,redirect, render_template, url_for,request,session
from flask_session import Session
from cs50 import SQL
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///project.db'
# db=SQLAlchemy(app)
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)


   


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
