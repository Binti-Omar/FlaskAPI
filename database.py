from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    ___tablename___='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)    
    email = db.Column(db.String(120),unique=True,nullable=False)
    password = db.Column(db.String(55), nullable=False)