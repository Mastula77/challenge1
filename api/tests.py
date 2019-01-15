import unittest
from models import user
import json


class TestUser(unittest.TestCase):
    def setUp(self):
        """
        Setting up a test client
        """
        
        self.test_client = self.app.test_client()
   
    def test_home(self):
        response = self.test_client.get(
            '/api/v1/'
        )

        reply = json.loads(response.data.decode())
        self.assertEqual(reply['message'], "Welcome to mastula's iReporter app.")
        self.assertEqual(response.status_code, 200)

    def test_create_user_empty_username(self):
        """
        Test if a user can be created with empty username.
        """
        user = {
            "firstname": "logose",
            "lastname": "mastula",
            "othernames": "mercy",
            "email": "logosemastula@gmail.com",
            "phoneNumber": "0752230290",
            "username": "",
            "isAdmin": "true",
    
        }

        response = self.test_client.post(
            'api/v1/signup',
            content_type='application/json',
            data=json.dumps(user)
        )
        message = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 400)
        self.assertEqual(message['Error'], 'Please fill in username field!')

    def test_create_user(self):
        """
        Test if a user can be registered successfully.
        """
        user = {
            "firstname": "Gimbo",
            "lastname": "shakira",
            "othernames": "destiny",
            "email": "shakiragim@gmail.com",
            "phoneNumber": "0779054030",
            "username": "shakii",
            "isAdmin": "False",
            "registered":"12/01/2019"
        }
        response = self.test_client.post(
            'api/v1/signup',
            content_type='application/json',
            data=json.dumps(user)
        )
        message = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(message['message'], 'favor successfully registered.')


