#!/usr/bin/python3
"""Starts a Flask web app listening on 0.0.0.0:5000"""

from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/', strict_slashes=False)
def hello_flask():
    """Displays “Hello HBNB!”"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays “HBNB”"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """Displays “C ” followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/(<text>)', strict_slashes=False)
def python_is_cool(text="is cool"):
    """Displays “Python ”, followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_it_a_number(n):
    """Displays “n is a number” only if n is an integer."""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """Displays a HTML page only if n is an integer."""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
<<<<<<< HEAD
    
=======
>>>>>>> aecb5e35a0592cc76f51b4d349130253814a8da8
