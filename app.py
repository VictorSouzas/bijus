# coding: utf-8
from flask import Flask
from blueprints.usuarios import usuarios_blueprint

def create_app(mode):
    app = Flask(__name__)
    app.config.from_pyfile("%s.cfg" % mode)
    return app