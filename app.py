from turtle import end_fill
from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = []

@app.get('/')
def show_start():
    """display survey title, instructions, and start button"""


# @app.post(dkfjnsdfkjnsf)
#     redirect to next question

# @app.get(/questions/<question_index>)
#     if question_index == survey.questions.length:
#         go to end
#     else:
#         go to /q/questionsuestion_index+1


# @app.get(end)
#     display end