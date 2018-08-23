import unittest
import json
from run import APP
"""
Class for all gets and Post
"""
class TestViews(unittest.TestCase):
  

    def setUp(self):

        self.question = APP
        self.client = self.question.test_client
    """
    methods defines test cases for get all questions
    """
    def test_getallquestions(self):

        result = self.client().get('/api/v1/questions/')
        self.assertEqual(result.status_code,200)
       # self.assertTrue(result.json["questions"])

    """
    methods defines test cases for get a question
    """
        
    def test_getaquestion(self):

        result = self.client().get('/api/v1/questions/2')
        self.assertEqual(result.status_code,301)
        #self.assertTrue(result.json["question"])
        
    """
    methods defines test cases for post a question
    """

    def test_postquestion(self):

        result = self.client().post('/api/v1/questions/', content_type="application/json", data=json.dumps(
            dict(author="natasha", question="what is boot camp",question_id="1",)))
        self.assertEqual(result.status_code, 200)
        self.assertTrue(result.json["questions"])
        self.assertIn('question', str(result.data))
    """
    methods defines test cases for posts an answer to a question
    """

    def test_post(self):

        result = self.client().post('/api/v1/questions/3/answers', content_type="application/json",
        data=json.dumps(dict( author="mukasa", question="what is boot camp?",question_id=4,answer="boot camp is process to andela")))

        