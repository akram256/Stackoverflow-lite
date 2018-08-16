"""
Module decorates views to urls
"""
from views import GetAllquestion

class GetUrls:
    """
    Method that views with urls
    """
    @staticmethod
    def fetch_urls(question):
        """
        Method that views with urls
        """
        questions_view = GetAllquestion.as_view('questions')
        question.add_url_rule('/ui/api/questions/', view_func=questions_view, defaults={'question_id': None}, methods=['GET',])
        question.add_url_rule('/ui/api/questions/<int:question_id>', view_func=questions_view, methods=['GET',])
        question.add_url_rule('/ui/api/questions/', view_func=questions_view, methods=['POST',])