import os
from app import create_app
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
    	self.app = create_app('teste')
        self.db_fd, self.app.config['SQLALCHEMY_DATABASE_URI'] = tempfile.mkstemp()
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
    	assert '<User victor>' in rv.data

if __name__ == '__main__':
    unittest.main()