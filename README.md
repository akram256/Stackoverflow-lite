# Stackoverflow-lite
https://akram256.github.io/Stackoverflow-lite-ui-/
[![Coverage Status](https://coveralls.io/repos/github/akram256/Stackoverflow-lite/badge.svg?branch=api)](https://coveralls.io/github/akram256/Stackoverflow-lite?branch=api)
[![Build Status](https://travis-ci.org/akram256/Stackoverflow-lite.svg?branch=api)](https://travis-ci.org/akram256/Stackoverflow-lite)
[![Maintainability](https://api.codeclimate.com/v1/badges/92c0f859c1d81c3ecd00/maintainability)](https://codeclimate.com/github/akram256/Stackoverflow-lite/maintainability)


Stackoverflow is a question answering platform, this is where someones asks a question, then people can comments, answer` down vote or upvte a question


**Features**

 user signup
 
 userlogin
 
 post a question
 
 answer a question
 
 downvote and upvote a question
 
 view number and author of questions
 
 view number and authors of an answer to a question
 
 
 **API end points**

GET /api/v1/questions
GET /api/v1/questions/<questionId>
POST /api/v1/questions/<questionId>/answers
POST /api/v1/users/questions

**Getting Started**

These instructions will enable you to run the project on your local machine.

**Prerequisites**

Below are the things you need to get the project up and running.

git : To update and clone the repository
python2.7 or python3: Language used to develop the api
pip: A python package used to install project requirements specified in the requirements text file.
Installing the project

Type:

    "git clone https://github.com/akram256/stackoverflow-lite-ui.git"
in the terminal or git bash or command prompt.
To install the requirements. run:
    pip install -r requirements.txt
cd to the folder stackoverflow-lite-ui And from the root of the folder, type:

  python run.py
To run the tests and coverage, from the root folder, type:

    pytest --cov=api/
