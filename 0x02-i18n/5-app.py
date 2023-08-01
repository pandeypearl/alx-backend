#!/usr/bin/env python3
""" Basic Flask Application """

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)


class Config(object):
    """ Configuration class for Babel object """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.before_request
def before_request():
    """ Determines if user is logged in, and what language """
    id = request.args.get('login_as')
    user = get_user(id)
    if user:
        g.user = user


def get_user(id):
    """ Returns user dictionary or None """
    if id and int(id) in users:
        return users[int(id)]
    return None


@app.route('/')
def hello_world():
    """ Render basic html file """
    login = False
    if g.get('user') is not None:
        login = True
    return render_template('5-index.html', login=login)


@babel.localeselector
def get_locale():
    """ Determines the best match with supported laguages """
    if request.full_path.split('/')[1][:8] == "?locale=":
        lang = request.full_path.split('/')[1][8:]
        if lang in app.config['LANGUAGES']:
            return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
