import os
from flask import Flask,redirect, render_template, url_for,request,session
# from flask_session import Session
# from cs50 import SQL
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime




app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///project.db'
# db=SQLAlchemy(app)
app.config["TEMPLATES_AUTO_RELOAD"]=True
app.jinja_env.filters["usd"]=usd
app.config["SESSION_PERMANENT"]=False
app.config["SESSION_TYPE"]="filesystem"
Session(app)

db=SQL("sqlite:///project.db")

# class Todo(db.Model):
#     id=db.Coloumn(db.Integer,primary_key=True)
#     content=db.Column(db.String(200,nullable=False))
#     completed = db.Column(db.Integer,default=0)
#     date_created=db.Column(db.DateTime,default=datetime.utcnow)

#     def __repr__(self):
#        return '<Task %r>' % self.id


   


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
