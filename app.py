from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story


app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh-so-secret'

debug = DebugToolbarExtension(app)


@app.route('/')
def index():
    """s.prompts - array of questions 
    dynamically html form - names"""
    prompts = story.prompts
    print(prompts)
    return render_template("form.html", prompts=prompts)

@app.route('/story')
def get_data():
    answers = story.generate(request.args)
    print(answers)
    return render_template("result.html", answers=answers)