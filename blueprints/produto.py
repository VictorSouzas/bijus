#coding: utf-8
from flask import (
    Blueprint,
    request,
    current_app,
    send_from_directory,
    render_template,
    session,
    url_for
    )

CadastroProduto_blueprint = Blueprint('CadastroProduto', __name__)
@CadastroProduto_blueprint.route('/admin/produto/cadastro/', methods=['GET', 'POST'])
def CadastroProduto():
	if request.method == 'POST':
		dados = request.form.to_dict()
		return 'cadastro efetuado com sucesso'
	else:
		return render_template()