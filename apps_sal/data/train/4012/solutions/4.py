import re


def encrypt(text, key):
    (a, b, c, d) = (ord(t) - 65 for t in key.upper())
    r = ''
    for (x, y) in zip(*[iter(re.findall('[A-Z]', text.upper()) + ['Z'])] * 2):
        (x, y) = (ord(t) - 65 for t in (x, y))
        (x, y) = ((a * x + b * y) % 26, (c * x + d * y) % 26)
        r += chr(x + 65) + chr(y + 65)
    return r
