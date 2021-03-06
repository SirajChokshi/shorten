import random
import sqlite3

NOUNS = 'nouns'
ADVERBS = 'adverbs'
VERBS = 'verbs'
LIST_SIZE = 1000

# returns a hyphenated phrase <string> from three received indexes <int>
def get_words(noun_index, adverb_index, verb_index):
    db = sqlite3.connect('./app/words.db')
    c = db.cursor()

    phrase = ""

    tags = {
        NOUNS: noun_index,
        ADVERBS: adverb_index,
        VERBS: verb_index
    }

    for tag in tags:
        c.execute("SELECT * FROM '{}' WHERE rowid={}".format(tag, tags[tag]))
        phrase += c.fetchone()[0] + "-"
    db.close()
    return phrase[:-1]

# returns three random indexes relative to the specified LIST_SIZE <int> constant
def gen_index():
    noun_index = random.randrange(0, LIST_SIZE) + 1
    adverb_index = random.randrange(0, LIST_SIZE) + 1
    verb_index = random.randrange(0, LIST_SIZE) + 1
    return noun_index, adverb_index, verb_index

# returns a random hyphenated phrase consisting of a noun, adverb, and verb
def gen_words():
    n, a, v = gen_index()
    return get_words(n,a,v)