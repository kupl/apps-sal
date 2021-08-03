from string import ascii_lowercase as aLow
import re


def rotateWord(w, alpha, dct, d):
    return ''.join((str.lower if w[i - 1].islower() else str.upper)(alpha[(dct[c] + i * d) % 26]) for i, c in enumerate(w.lower(), 1))


def encode(text, key, d=1):
    s = set(aLow)
    alpha = ''.join(s.remove(c) or c for c in key + aLow if c in s)
    dct = {c: i for i, c in enumerate(alpha)}
    return re.sub(r'[a-zA-Z]+', lambda m: rotateWord(m.group(), alpha, dct, d), text)


def decode(text, key):
    return encode(text, key, -1)
