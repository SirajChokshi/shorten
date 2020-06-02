import process_words
import sqlite3

# DISABLED FOR DATA SAFETY

# # print(process_words.test())

# conn = sqlite3.connect('../words.db')

# c = conn.cursor()

# words = {
#     'nouns': process_words.genList('../static/index.noun'),
#     'adverbs': process_words.genList('../static/index.adv'),
#     'verbs': process_words.genList('../static/index.verb'),
# }

# for tag in words:

#     # Create table
#     c.execute('''CREATE TABLE {}
#              (word text)'''.format(tag))

#     # Insert rows of data
#     for word in words[tag]:
#         c.execute("INSERT INTO {} VALUES ('{}')".format(tag, word))

# # Save (commit) the changes
# conn.commit()

# # We can also close the connection if we are done with it.
# # Just be sure any changes have been committed or they will be lost.
# conn.close()