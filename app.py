# coding: utf-8
from flask import Flask
from blueprints.usuarios import admin_blueprint
from blueprints.usuarios import login_blueprint
from blueprints.produto import CadastroProduto_blueprint
def create_app(mode):
    app = Flask('bijus')
    app.config.from_pyfile("%s.cfg" % mode)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(login_blueprint)
    app.register_blueprint(CadastroProduto_blueprint)
    
    return app