import sqlite3
import re
from . import gen_words

DATABASE = './app/links.db'

# returns True <bool> if the received url <string> is a valid URL, else returns False <bool>
def is_url_valid(url):
    REGEX_URL = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return (re.match(REGEX_URL, url) is not None)

# returns True <bool> if the received code <string> is a valid code, else returns False <bool>
# a valid code contains letters, numbers, or the specified symbols. Length must be greater than 0
def is_code_valid(code):
    REGEX_CODE = re.compile(r"[A-Za-z0-9$\-_.+*'(),]+")

    return bool(REGEX_CODE.fullmatch(code))

# returns True <bool> if the received code <string> exists in a row in the links table, else False <bool>
def is_code_used(code):
    links_db = sqlite3.connect(DATABASE)
    cur = links_db.cursor()
    cur.execute("SELECT EXISTS(SELECT 1 FROM links WHERE code='{}')".format(code.lower()))
    out = cur.fetchone()
    links_db.commit()
    links_db.close()
    try:
        return bool(out[0])
    except:
        return -1

# adds received url <string> and code <string> as a row in the links table
# return the entry's final code <string> on success, returns -1 <int> if URL is 
# invalid, returns -2 <int> if code exists in db, returns -3 <int> if code is not valid
def add_entry(url, code = -1):
    code_auto_generated = 0
    if code == -1:
        code = gen_words.gen_words()
        while is_code_used(code):
            code = gen_words.gen_words()
        code_auto_generated = 1

    if is_url_valid(url):
        if is_code_valid(code):
            if not is_code_used(code):
                links_db = sqlite3.connect(DATABASE)
                cur = links_db.cursor()
                cur.execute("INSERT INTO links VALUES ('{}','{}','{}')".format(code.lower(), url, code_auto_generated))
                links_db.commit()
                links_db.close()
                return code
            else:
                return -2
        else:
            return -3
    else:
        return -1

# returns entry for the received code <string>, returns -1 <int> if code is not present in database
def get_entry(code):
    links_db = sqlite3.connect(DATABASE)
    cur = links_db.cursor()
    cur.execute("SELECT * FROM links WHERE code='{}'".format(code.lower()))
    out = cur.fetchone()
    links_db.commit()
    links_db.close()
    try:
        return out[1]
    except:
        return -1