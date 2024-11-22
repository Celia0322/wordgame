from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

words = {
    "animals": ["Cat", "Dog", "Elephant", "Lion", "Tiger"],
    "colors": ["Red", "Blue", "Green", "Yellow", "Purple"],
    "fruits": ["Apple", "Banana", "Cherry", "Grape", "Orange"],
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    category = request.json.get('category')
    return jsonify({"words": words[category], "category": category})

@app.route('/check_answer', methods=['POST'])
def check_answer():
    category = request.json.get('category')
    word = request.json.get('word')
    answer = request.json.get('answer')
    if answer == category:
        return jsonify({"result": "Correct!"})
    else:
        return jsonify({"result": "Try again!"})

if __name__ == '__main__':
    app.run(debug=True)

