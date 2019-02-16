from boggle import Boggle

from flask import Flask, request, render_template, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"

debug = DebugToolbarExtension(app)

boggle_game = Boggle()

@app.route("/")
def show_board():
    """ print board to landing page"""

    board = boggle_game.make_board()

    session["board_session"] = board

    return render_template("landing.html", board = board)

@app.route("/", methods=["POST"])
def retrieve_guess():
    """ print the data from AJAX call"""
    input_word = request.form["guess"]
    check_for_word = boggle_game.check_valid_word(session['board_session'], input_word)
    # print(check_for_word)
    # import pdb; pdb.set_trace()

    response_message = {"result": check_for_word}


    return jsonify(response_message)

@app.route("/end", methods=["POST"])
def retrieve_game_data():
    """ print the data from AJAX call"""

    end_score = request.form["end_score"]
    session['high_score'] = max(session['high_score'], end_score)
    session['time_played'] = 1 + session['timed_playes'] or 1

    response_message = {"result": check_for_word}


    return jsonify(response_message)
