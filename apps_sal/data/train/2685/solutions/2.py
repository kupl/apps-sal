from string import ascii_lowercase as low
from itertools import filterfalse, chain

def keyword_cipher(msg, keyword):
    D = dict.fromkeys(keyword)
    cypher = ''.join(chain(D.keys(), filterfalse(D.__contains__, low)))
    return msg.lower().translate(str.maketrans(low, cypher))
