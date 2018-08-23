
"""end points for the questions"""
from flask import jsonify
from flask import request, Request
from flask.views import MethodView

class GetAllquestion(MethodView):
    """class for getting questions"""
    questions = []

    def get(self, question_id):
        """
        method for all get requests"
        """
        if question_id == None:
            return jsonify({'questions':[question for question in self.questions]})
        quiz = [question for question in self.questions if question['question_id'] == question_id]
        return jsonify({'question' : quiz[0]})

    def post(self):
        """method for all post requests"""
        if not request.json:
            return jsonify({'error':"not a json request"}), 400
        else:
            question = {'author':request.json['author'], 'question' : request.json['question'],
                        'question_id':request.json['question_id']}
            self.questions.append(question)
            return jsonify({'questions' : self.questions})

class GetAllanswers(MethodView):
    """ class for getting all answers"""
    answers = []
    def post(self, question_id):
        """ method for all post answers"""
        if not request.json:
            return jsonify({'error':"not a json request"}), 400
        else:
            answer = {'author':request.json['author'], 'answer' :request.json['answer'],
                      'question_id':question_id}
            self.answers.append(answer)
            return jsonify({'answers' : self.answers})
