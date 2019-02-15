from boggle import Boggle

from flask import Flask, request, render_template, session
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

@app.route("/hello", methods=["POST"])
def retrieve_guess():
    """ print the data from AJAX call"""

    import pdb; pdb.set_trace()
    say_hello = request.form["guess"]

    return say_hello