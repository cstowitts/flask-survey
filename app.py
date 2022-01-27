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

    survey_title = survey.title
    survey_instructions = survey.instructions

    return render_template("survey_start.html", survey_title=survey_title, survey_instructions=survey_instructions)


#   this will happen in the POST request when continue button is pressed
#     if question_index == survey.questions.length:
#         go to end
#     else:
#         go to /q/questionsuestion_index+1

@app.get('/questions/<int:question_index>')
def show_question(question_index):
    """display appropriate question, choices, and continue button"""

    survey_question = survey.questions[question_index]
    
    return render_template("question.html", question=survey_question)


@app.post('/answer')
def store_answer():
    """Stores user's answer in responses and redirects to next question"""

    answer = request.form["answer"]
    responses.append(answer)
    next_question_index = len(responses)
    
    if len(survey.questions) == len(responses):
        return redirect("/thanks")
    else:
        return redirect(f"/questions/{next_question_index}")
    
@app.get('/thanks')
def display_thanks():
    return "thnkx"

# @app.get(end)
#     display end