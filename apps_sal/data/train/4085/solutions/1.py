from re import sub
from random import shuffle


def scramble(m):
    s = list(m.group())
    shuffle(s)
    return ''.join(s)


def mix_words(string):
    return sub('\B\w+\B', scramble, string)
