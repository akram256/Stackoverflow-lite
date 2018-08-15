"""This is the main module"""
import unittest
import json
from json import JSONEncoder

from app import APP
class TestViews(unittest.TestCase):
    """
    Class defines test cases
    """
    def setUp(self):
        """
        initializing
        """
        self.ride = APP
        self.client = self.question.test_client
    def test_get_all_clients(self):
        """
        method for testing get all questions
        """
        result = self.client().get('/ui/api/questions'')
        self.assertEqual(result.status_code, 200)
        self.assertTrue(result.json["questions"])