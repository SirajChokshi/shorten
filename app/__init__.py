# 3rd party imports
from flask import Flask, redirect, render_template, request, abort, jsonify
# local imports
from . import access_database

app = Flask(__name__)

# homepage
@app.route("/")
def home():
    return render_template('index.html', result = -3)

# terms of use
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
# paired, aborts with a HTTP status 404.
@app.route("/<code>")
def redirect_from_code(code):
    destination = access_database.get_entry(code)
    if destination != -1:
        return redirect(destination)
    else:
        abort(404)

# handle 404 status codes by rendering the styled page
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# register the error handler with flask
app.register_error_handler(404, page_not_found)

'''
api endpoint for creating a new shortened link
returns the the created link if successful, or an error code from access_database.add_entry()
'''
@app.route("/api/create", methods=['POST'])
def handle_api_data():
    input_url = request.args.get("url")
    input_code = request.args.get("code")

    # if the code is invalid, sets the code to the default value so add_entry generates a code
    if(input_code == None or len(input_code) == 0):
        input_code = -1

    final_code = access_database.add_entry(input_url,input_code)
    # if successfuly shortened, return the short link
    if(isinstance(final_code, str)):
        final_url = request.url_root + final_code

    return jsonify(shortenedUrl=final_url)