#!/usr/bin/env python3
""" PAramiterize templates based on request parameters """
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _
import os
Config = __import__("1-app").Config

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_user():
    """ gets the logged-in user from db """
    user = request.args.get("login_as")
    try:
        return users.get(int(user))
    except Exception as e:
        return None


@app.before_request
def before_request():
    """ get a user and set it as a golbal on flask.g.user """
    user = get_user()
    g.user = user.get('name') if user else None


@babel.localeselector
def get_locale():
    """ Gets the locale  based on a query parameter"""
    locale = request.args.get("locale")
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    else:
        locale = os.getenv("LANGUAGE").split(":")[0]
        if locale:
            return locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/", strict_slashes=False)
def index():
    """ index view """
    home_title = _("Welcome to Holberton")
    home_header = _("Hello world!")

    if g.user:
        message = _("You are logged in as %(username)s.") % {
                "username": g.user
                }
    else:
        message = _("You are not logged in.")
    return render_template(
            "5-index.html",
            home_title=home_title, home_header=home_header, message=message)


if __name__ == "__main__":
    app.run(port='5000', debug=True)
