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
        self.login = login
        self.email = email
        self.senha = senha

class Produto(object):
    """docstring for Product"""
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(60), unique=True)
    descrissao = db.Column(db.Text)
    peso = db.Column(db.Float)
    estoque = db.Column(db.Integer)
    data = db.Column(db.DateTime)
    imagem = db.Column(db.String(50))
    preco = db.Column(db.Float)
    metatags = db.Column(db.String(60))
    metadescription = db.Column(db.Text)
    slug_url = db.Column(db.String(70))
    categoria_id = db.Column(db.Integer, db.ForeignKey('categoria.id'))

    def __init__(self, nome, descrissao, peso, estoque, imagem, preco, metatags, metadescription, slug_url, categoria_id):
        self.nome = nome
        self.descrissao = descrissao
        self.peso = peso
        self.estoque = estoque
        self.imagem = imagem
        self.preco = preco
        self.metatags = metatags
        self.metadescription = metadescription
        self.slug_url = slug_url
        self.categoria_id = categoria_id 
