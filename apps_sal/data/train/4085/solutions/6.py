import re
from random import sample


def mix_words(strng):
    if type(strng) != str:
        return None
    return re.sub('[A-Za-z]{4,}', fu, strng)


def fu(w):
    w = w.group()
    r = w[1:-1]
    while r == w[1:-1]:
        r = ''.join(sample(r, len(r)))
    return w[0] + r + w[-1]
