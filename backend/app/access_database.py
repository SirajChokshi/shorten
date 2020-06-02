import sqlite3
import re
import gen_words


DATABASE = 'links.db'
code = "Siraj"
url = "https://sirajchokshi.com"

def is_url_valid(url):
    REGEX_URL = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return (re.match(REGEX_URL, url) is not None)

def is_code_used(code):
    links_db = sqlite3.connect(DATABASE)
    cur = links_db.cursor()
    cur.execute("SELECT EXISTS(SELECT 1 FROM links WHERE code='{}')".format(code.lower()))
    out = cur.fetchone()
    links_db.commit()
    links_db.close()
    return bool(out[0])

def add_entry(url, code = gen_words.gen_words()):
    if is_url_valid(url) and not is_code_used(code):
        links_db = sqlite3.connect(DATABASE)
        cur = links_db.cursor()
        cur.execute("INSERT INTO links VALUES ('{}','{}')".format(code.lower(), url))
        links_db.commit()
        links_db.close()
