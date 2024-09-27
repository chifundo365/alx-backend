#!/usr/bin/env python3
""" PAramiterize templates based on request parameters """
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _
Config = __import__("1-app").Config


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Gets the locale  based on a query parameter"""
    locale = request.args.get("locale")

    if locale and locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", strict_slashes=False)
def index():
    """ index view """
    home_title = _("Welcome to Holberton")
    home_header = _("Hello world!")
    return render_template(
            "4-index.html",
            home_title=home_title, home_header=home_header)


if __name__ == "__main__":
    app.run(port='5000', debug=True)
