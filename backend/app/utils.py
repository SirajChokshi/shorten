import time
import requests
import random

LIST_SIZES = 500

PROFANITY_WORDLIST_URL = 'https://raw.githubusercontent.com/snguyenthanh/better_profanity/master/better_profanity/profanity_wordlist.txt'
PROFANITY_WORDLIST = requests.get(PROFANITY_WORDLIST_URL, allow_redirects=True).content.decode().split('\n')[:-1]

def isProfane(str):
    for word in PROFANITY_WORDLIST:
        if word.lower() in str.lower():
            return True
    return False

def isValid(str):
    return str.isalpha() and (not isProfane(str)) and len(str) < 8 and len(str) > 3

def genList(file):
    start = time.time()
    adverb_file = open(file)
    line_list = adverb_file.read().split('\n')[30:]

    output = []
    i = 0

    while i < LIST_SIZES:
        index = random.randint(0, len(line_list) - 1)
        current_word = line_list[index].split(' ')[0]
        if isValid(current_word):
            output.append(current_word)
            i += 1
    end = time.time()
    print("List built with {}ms elapsed".format(end - start))
    return output

def test():
    nouns = genList('static/index.noun')
    adv = genList('static/index.adv')
    verbs = genList('static/index.verb')

    for j in range(0, LIST_SIZES):
        print(nouns[j], adv[j], verbs[j] + 's')

test()