import os
from flask import Flask,redirect, render_template, url_for,request,session
# from flask_session import Session
# from cs50 import SQL
from tempfile import mkdtemp
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///project.db'
with app.app_context():
    db=SQLAlchemy(app)
app.config["TEMPLATES_AUTO_RELOAD"]=True
# app.jinja_env.filters["usd"] = usd
# app.config["SESSION_PERMANENT"]=False
# app.config["SESSION_TYPE"]="filesystem"
# Session(app)

# db=SQL("sqlite:///project.db")

class Todo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(200),nullable=False)
    completed = db.Column(db.Integer,default=0)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self):
       return '<Task %r>' % self.id


   


@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='POST':
        task_content=request.form['content']
        new_task= Todo(content=task_content)
        
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    else:
        tasks=Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete =Todo.query.get_or_404(id)
    
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleteing that task'  
    


if __name__ == "__main__":
    app.run(debug=True)
