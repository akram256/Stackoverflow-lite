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
        question_view_update = (GetAllquestion.as_view('rides_update')
        question.add_url_rule('/ui/api/questions/', defaults={'question_id': None}, view_func=questions_view_update, methods=['POST',])