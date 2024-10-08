#!/usr/bin/env python3
""" PAramiterize templates """
from flask import Flask, render_template, request
from flask_babel import Babel, gettext
Config = __import__("1-app").Config


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Gets the locale """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", strict_slashes=False)
def index():
    """ index view """
    home_title = gettext("Welcome to Holberton")
    home_header = gettext("Hello world!")
    return render_template(
            "3-index.html",
            home_title=home_title, home_header=home_header)


if __name__ == "__main__":
    app.run(port='5000', debug=True)
