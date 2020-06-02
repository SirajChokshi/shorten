from flask import Flask, redirect
from . import access_database

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/<code>")
def redirect_from_code(code):
    destination = access_database.get_entry(code)
    if destination != -1:
        return redirect(destination)
    else:
        return redirect("/notfound")

@app.route("/notfound")
def not_found():
    return "This shortened link has not yet been created."