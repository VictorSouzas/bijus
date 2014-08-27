# coding: utf-8
import db.db as db
from flask import (
    Blueprint,
    request,
    current_app,
    send_from_directory,
    render_template
    )
admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route("/admin/cadastro/", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":

        dados = request.form.to_dict()

        login = dados['login']
        email = dados['email']
        senha = dados['senha']

        try:
            novo_usuario = db.Admin(login, email, senha)
            db.db.session.add(novo_usuario)
            db.db.session.commit()
            return '<User %s>' % login
        except Exception, e:
            db.db.session.rollback()
            raise e
        

    return render_template('cadastro.html', title=u"Inserir nova noticia")