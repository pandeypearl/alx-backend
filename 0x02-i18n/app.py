#!/usr/bin/env python3
""" Basic Flask Application """

from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime
import pytz
from datetime import datetime


class Config(object):
    """ Configuration class for Babel object """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Instantiate application object
app = Flask(__name__)
app.config.from_object(Config)

# Wrap applicatin with Babel
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


@babel.localeselector
def get_locale():
    """ Determines the best match with supported laguages """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if (g.get('user') and g.user.get("locale", None)
            and g.user["locale"] in app.config['LANGUAGES']):
        return g.user["locale"]
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """ Returns the time in timezone """
    try:
        if request.args.get('timezone'):
            return str(pytz.timezone(request.args.get('timezone')))
        if g.get('user') and g.user.get('timezone'):
            return str(pytz.timezone(g.user['timezone']))
    except pytz.exceptions.UnknownTimeZoneError:
        pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/', strict_slashes=False)
def hello_world():
    """ Render basic html file """
    login = False
    if g.get('user') is not None:
        login = True
    current = format_datetime(datetime.now())
    return render_template('index.html', login=login, current_time=current)


if __name__ == '__main__':
    app.run()
