# 3rd party imports
from flask import Flask, redirect
# local imports
from . import access_database

app = Flask(__name__)

# homepage
@app.route("/")
def hello():
    return "Hello, World!"

# redirects to the page that is linked to the code. if the code has not been 
# paired, redirects to the notfound page.
@app.route("/<code>")
def redirect_from_code(code):
    destination = access_database.get_entry(code)
    if destination != -1:
        return redirect(destination)
    else:
        return redirect("/notfound")

# notfound page
@app.route("/notfound")
def not_found():
    return "This shortened link has not yet been created."