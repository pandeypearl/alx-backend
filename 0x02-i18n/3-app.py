#!/usr/bin/env python3
""" Basic Flask Application """

from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """ Configuration class for Babel object """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Instatiate application object
app = Flask(__name__)
app.config.from_object(Config)

# Wrap applicatin with babel
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ Determines the best match with supported languages """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def hello_world() -> str:
    """ Render basic html file """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
