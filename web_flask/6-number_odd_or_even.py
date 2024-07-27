#!/usr/bin/python3
""" This script starts a flask web application """
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ home page for HBNB website """
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ defines content for hbnb route """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c_is(text):
    """ defines a c_is endpoint """
    output = text.replace("_", " ")
    return (f"C {output}")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """ defines a python endpoint """
    output = text.replace("_", " ")
    return (f"Python {output}")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ endpoint that checks for integer """
    return (f"{n} is a number")


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ renders a html template if n is an integer """
    return render_template("5-number.html", n=n)


@app.template_filter('even_odd')
def check_even_odd(n):
    """ checks whether integer passed is even or odd """
    if n % 2 == 0:
        return (f"{n} is even")
    else:
        return (f"{n} is odd")


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ Renders page depending on whether n is even or odd """
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
