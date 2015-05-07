# coding: utf-8
import db.db as db
from flask import (
    Blueprint,
    request,
    current_app,
    send_from_directory,
    render_template,
    session,
    url_for
    )
import hashlib

admin_blueprint = Blueprint('admin', __name__)
@admin_blueprint.route("/admin/cadastro/", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":

        dados = request.form.to_dict()

        login = dados['login']
        email = dados['email']

        instancia_hash = hashlib.md5()
        instancia_hash.update(dados['senha'])
        senha = instancia_hash.hexdigest()

        try:
            novo_usuario = db.Admin(login, email, senha)
            db.db.session.add(novo_usuario)
            db.db.session.commit()
            return 'sucesso'
        except Exception:
            db.db.session.rollback()
            return 'Não foi dessa vez tente novamente mais tarde'
    
    else:
        return render_template('admin/cadastro.html',
                     title=u"Novo usuario na base de dados.",
                     SimpleTitle=u"Cadastro de usuarios")

login_blueprint = Blueprint('login', __name__)
@login_blueprint.route('/admin/login/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        
        entrada = request.form.to_dict()

        login = entrada['login']
        instancia_hash = hashlib.md5()
        instancia_hash.update(entrada['senha'])
        senha = instancia_hash.hexdigest()
        try:
            usuario = db.Admin.query.filter_by(login=login,senha=senha).first()

            if usuario is None:
                return 'Usuario não encontrado'
            else:
                session['login'] = usuario.login
                session['hash'] = usuario.senha
                return 'sucesso'
        except Exception, e:
            return '%s' % e
        
    else:
        url = url_for('.login')
        return url