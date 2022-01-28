from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

# responses = []


@app.get('/')
def show_start():
    """display survey title, instructions, and start button"""
    session["responses"] = []

    survey_title = survey.title
    survey_instructions = survey.instructions

    return render_template(
        "survey_start.html",
        survey_title=survey_title,
        survey_instructions=survey_instructions)


@app.get('/questions/<int:question_index>')
def show_question(question_index):
    """display appropriate question, choices, and continue button"""
    num_answers = len(session["responses"])
    #The index of your next question will always be equal to the 
    #number of answers you have provided (length of responses list)
    if question_index != num_answers:
        return redirect(f"/questions/{num_answers}")
    else:
        survey_question = survey.questions[question_index]

        return render_template("question.html", question=survey_question)


@app.post('/answer')
def store_answer():
    """Stores user's answer in responses and redirects to next question"""

    answer = request.form["answer"]

    responses = session["responses"]
    responses.append(answer)
    session["responses"] = responses
    next_question_index = len(responses)

    if len(survey.questions) == len(responses):
        return redirect("/thanks")
    else:
        return redirect(f"/questions/{next_question_index}")


@app.get('/thanks')
def display_thanks():
    """empty responses list and render survey completion confirmation"""

    # global responses
    # responses = []

    return render_template("completion.html")

# @app.get(end)
#     display end
