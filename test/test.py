import unittest
from app import app, validate_token

class TestApp(unittest.TestCase):

    # Prueba para la función validate_token
    def test_validate_token(self):
        valid_token = jwt.encode({'some': 'payload'}, app.config['SECRET_KEY'], algorithm='HS256')
        response = validate_token(valid_token)
        self.assertNotIn('ERROR', response)

    # Prueba para la ruta /DevOps
    def test_devops_route(self):
        tester = app.test_client(self)
        headers = {
            'X-Parse-REST-API-Key': app.config['API_KEY'],
            'X-JWT-KEY': jwt.encode({'some': 'payload'}, app.config['SECRET_KEY'], algorithm='HS256')
        }
        response = tester.post('/DevOps', headers=headers, json={'message': 'Test Message', 'to': 'Test User'})
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', data)

if __name__ == '__main__':
    unittest.main()
