import string
from itertools import cycle


def encode(message, key):
    alphabet = dict(zip(string.ascii_lowercase, (ord(i) - 96 for i in string.ascii_lowercase)))
    key = cycle([int(i) for i in str(key)])
    res = []
    for i in message:
        encoding = int(alphabet.get(i)) + next(key)
        res.append(encoding)
    return res
