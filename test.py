from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True
    
    def tearDown(self):
        print('teared!!!!')
    
    def test_make_board(self):
        """making a board for test"""
        # #test client makes a request
        result = self.client.get('/')

        self.assertEqual(result.status_code, 200)
        print("client made!")

    def test_session(self):
        with self.client:
           response = self.client.get('/')
           self.assertIsInstance(session['board_session'], list) 


    # TODO -- write tests for every view function / feature!

