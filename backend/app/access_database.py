import sqlite3
import re
import gen_words

DATABASE = 'links.db'

# returns True if the received url <string> is a valid URL, else returns False
def is_url_valid(url):
    REGEX_URL = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return (re.match(REGEX_URL, url) is not None)

# returns True if the received code <string> exists in a row in the links table, else False
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
# return 0 on success, returns -1 if URL is invalid, returns -2 if code exists in db
def add_entry(url, code = -1):
    if code == -1:
        code = gen_words.gen_words()
        while not is_code_used(code):
            code = gen_words.gen_words()
    if is_url_valid(url):
        if not is_code_used(code):
            links_db = sqlite3.connect(DATABASE)
            cur = links_db.cursor()
            cur.execute("INSERT INTO links VALUES ('{}','{}')".format(code.lower(), url))
            links_db.commit()
            links_db.close()
            return 0
        else:
            return -2
    else:
        return -1

# returns entry for the received code, returns -1 if code is not present in database
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