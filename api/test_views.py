import unittest
import json
from app import APP

class TestViews(unittest.TestCase):
    """
    Class defines test cases for gets and posts
    """

    def setUp(self):

        self.question = APP
        self.client = self.question.test_client

    def test_get(self):


        result = self.client().get('/ui/api/questions/')
        self.assertEqual(result.status_code, 200)
        self.assertTrue(result.json["questions"])
        
    def test_get(self):

        result = self.client().get('/ui/api/questions/2')
        self.assertEqual(result.status_code, 200)
        self.assertTrue(result.json["question"])

    def test_post(self):

        result = self.client().post('/ui/api/questions/', content_type="application/json", data=json.dumps(
            dict(author="natasha", question="what is boot camp",question_id="1",)))
        self.assertEqual(result.status_code, 200)
        self.assertTrue(result.json["questions"])
        self.assertIn('question', str(result.data))
        
    def test_post(self):
        result =self.client().post('/ui/api/questions/3/answers', content_type="application/json",
        data=json.dumps(dict( author="mukasa", question="what is boot camp?",question_id=4,answer="boot camp is process to andela")))

        