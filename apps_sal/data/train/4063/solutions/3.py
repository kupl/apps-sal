import re

def fix(word):
    word = ''.join(c for c in word if c.isalnum())
    if len(word) % 2:
        word += word[-1]
    return word

def evenator(s):
    return ' '.join(filter(None, map(fix, s.split())))
