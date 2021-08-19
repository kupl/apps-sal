import re
from collections import OrderedDict
from string import ascii_lowercase


def encode(text, key, mul=1):
    i2c = ''.join(OrderedDict.fromkeys(key)) + ''.join((c for c in ascii_lowercase if c not in key))
    c2i = {c: i for (i, c) in enumerate(i2c)}
    return re.sub('[a-z]+', lambda m: ''.join(((str.upper if c.isupper() else str)(i2c[(c2i[c.lower()] + i * mul) % 26]) for (i, c) in enumerate(m.group(), 1))), text, flags=re.I)


def decode(text, key):
    return encode(text, key, -1)
