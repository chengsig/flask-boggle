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

    return render_template("landing.html", board = board)