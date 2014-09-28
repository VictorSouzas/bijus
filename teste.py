import os
from app import create_app
import flask
import unittest
import tempfile
import hashlib
import db.db as db

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
    	self.app = create_app('teste')
        self.db_fd, self.app.config['SQLALCHEMY_DATABASE_URI'] = tempfile.mkstemp()
        db.db.create_all()
        self.app.config['TESTING'] = True
        self.app = self.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)

    def CadastroAdmin(self, login, email, senha):
    	return self.app.post('/admin/cadastro/', data=dict(
    		login=login,
    		email=email,
    		senha=senha
    		))

    def test_CadastroAdmin(self):
    	rv = self.CadastroAdmin('victor', 'victor_souzas@yahoo.com.br', 'hashmd5')
    	assert 'sucesso' in rv.data

    def test_Login_Admin(self):
        with self.app:
            r = self.app.post('/admin/login/', data=dict(
                login='victor',
                senha='hashmd5'
                ))
            instancia_hash = hashlib.md5()
            instancia_hash.update('hashmd5')
            senha = instancia_hash.hexdigest()
            assert flask.session['login'] == 'victor'
            assert flask.session['hash'] == senha

    def CadastroProduto(self, nome, descrissao, peso, estoque, imagem, preco, metatags, metadescription, slug_url, categoria_id):
        return self.app.post('/admin/produto/cadastro/', data=dict(
            nome = nome,
            descrissao = descrissao,
            peso = peso,
            estoque = estoque,
            imagem = imagem,
            preco = preco,
            metatags = metatags,
            metadescription = metadescription,
            slug_url = slug_url, 
            categoria_id = categoria_id
            ))
    def test_CadastroProduto(self):
        rv = self.CadastroProduto(
            'colar de brinquedo',
            'colar feito de balas de chocolate',
            '1,93',
            '30',
            'chocolate.jpg',
            '34,00',
            'chocolate, colar, balas, crianca',
            'colar balas chocolate',
            'colar-balas-chocolate',
            '1'
            )
        assert 'cadastro efetuado com sucesso' in rv.data 

if __name__ == '__main__':
    unittest.main()