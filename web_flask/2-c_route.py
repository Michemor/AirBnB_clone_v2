#!/usr/bin/python3
""" This script starts a flask web application """
from flask import Flask


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
    output = text.replace("_", " ")
    return (f"C {output}")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
