# 3rd party imports
from flask import Flask, redirect, render_template, request
# local imports
from . import access_database

app = Flask(__name__)

# homepage
@app.route("/")
def home():
    return render_template('index.html', result = -3)

# privacy policy
@app.route("/terms")
def terms():
    return render_template('terms.html')

# handle link creation
@app.route('/', methods=['POST'])
def handle_data():
    url = request.form['url']
    code = request.form['code']
    output = -5
    if len(code) < 1:
        output = access_database.add_entry(url)
    else:
        output = access_database.add_entry(url, code)
    return render_template('index.html', result = output, url = url)

# redirects to the page that is linked to the code. if the code has not been 
# paired, redirects to the 404 page.
@app.route("/<code>")
def redirect_from_code(code):
    destination = access_database.get_entry(code)
    if destination != -1:
        return redirect(destination)
    else:
        return redirect("/404")

@app.route("/404")
def not_found():
    return "This shortened link has not yet been created."