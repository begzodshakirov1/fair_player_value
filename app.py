from flask import Flask, render_template, request
from names import get_player_names

website = Flask(__name__)

@website.route("/")
def main_page():
        return render_template("index.html")

@website.route("/list")
def list():
        inputname = request.args.get('player_name')
        return get_player_names(inputname).to_html(index = False)