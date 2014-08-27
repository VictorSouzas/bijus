#coding: utf-8

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

class Admin(db.Model):
    """docstring for Admin"""
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    senha = db.Column(db.String(120), unique=False)

    def __init__(self, login, email, senha):
        try:
            db.create_all()
        except Exception, e:
            pass
        finally:
            self.login = login
            self.email = email
            self.senha = senha
