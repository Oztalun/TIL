from flask import Flask, render_template, request, jsonify, session
import random
from hangman import words, initialize_game, check_guess, update_game_state

app = Flask(__name__)
app.secret_key = 'supersecretkey'


@app.route('/')
def index():
    session['answer'], session['submit'], session['chances'], session['used_alphabets'] = initialize_game(words)
    return render_template('index.html')


@app.route('/guess', methods=['POST'])
def guess():
    guess = request.json['guess']
    answer = session['answer']
    submit = session['submit']
    chances = session['chances']
    used_alphabets = session['used_alphabets']

    if guess in used_alphabets:
        return jsonify({'message': '이미 사용한 알파벳입니다.', 'status': 'used'})

    used_alphabets.append(guess)
    is_correct, submit = check_guess(answer, submit, guess)

    if not is_correct:
        chances -= 1

    session['submit'] = submit
    session['chances'] = chances
    session['used_alphabets'] = used_alphabets

    game_over = chances == 0 or submit == answer
    return jsonify({
        'submit': ''.join(submit),
        'chances': chances,
        'used_alphabets': used_alphabets,
        'game_over': game_over,
        'message': '맞았습니다!' if is_correct else '정답에 포함된 알파벳이 아닙니다. 기회가 차감됩니다.'
    })


if __name__ == '__main__':
    app.run(debug=True)
