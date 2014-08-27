# coding: utf-8
from flask import Flask
from blueprints.usuarios import admin_blueprint

def create_app(mode):
    app = Flask(__name__)
    app.config.from_pyfile("%s.cfg" % mode)
    app.register_blueprint(admin_blueprint)
    return app