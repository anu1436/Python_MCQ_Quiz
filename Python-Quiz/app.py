from flask import Flask, render_template, jsonify
import json
import random

app = Flask(__name__)

# Load questions from the JSON file
def load_questions():
    with open('python_questions.json') as file:
        return json.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/api/questions')
def api_questions():
    questions = load_questions()
    random.shuffle(questions)  # Shuffle the questions
    return jsonify(questions)

if __name__ == '__main__':
    app.run(debug=True)
