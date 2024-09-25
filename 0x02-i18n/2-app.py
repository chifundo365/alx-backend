#!/usr/bin/env python
""" Basic Flask, Babel Application """
from flask import Flask, request, render_template
from flask_babel import Babel
Config = __import__("1-app").Config

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ gets the locale """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """ index view """
    print(get_locale())
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(port='5000')

