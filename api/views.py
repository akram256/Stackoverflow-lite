from flask import jsonify
from flask import Flask, request, Request
from flask.views import MethodView

class GetAllquestion(MethodView):
   
    questions =[
        { "author":"Akram","question":"how long is boot camp","question_id":1},
        { "author":"Mukasa","question":"what is Andela","question_id":2},
        { "author":"Natasha","question":"what is the use of pip freeze","question_id":3}
      ]     
    def get(self,question_id):
        """
        method for all get requests"
        """
        if question_id == None:
           return jsonify({'questions':[question for question in self.questions]})
        quiz = [question for question in self.questions if question['question_id'] == question_id]
        return jsonify({'question' : quiz[0]})


