"""end points for the questions"""
from flask import jsonify
from flask import request, Request
from flask.views import MethodView

class GetAllquestion(MethodView):
    """class for getting questions"""
    questions = [
        {"author":"Akram", "question":"how long is boot camp", "question_id":1},
        {"author":"Mukasa", "question":"what is Andela", "question_id":2},
        {"author":"Natasha", "question":"what is the use of pip freeze", "question_id":3}]

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
    answers = [{"author":"Mukasa", "answer":"Andela is a software agency", "question_id":4},
               {"author":"Natasha", "answer":"technology has easied life", "question_id":5},
               {"author":"Axsam", "answer":"i like andela", "question_id":6}]
    def post(self, question_id):
        """ method for all post answers"""
        if not request.json:
            return jsonify({'error':"not a json request"}), 400
        else:
            answer = {'author':request.json['author'], 'answer' :request.json['answer'],
                      'question_id':question_id}
            self.answers.append(answer)
            return jsonify({'answers' : self.answers})
