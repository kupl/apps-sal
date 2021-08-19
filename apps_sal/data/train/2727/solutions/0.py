from collections import Counter
from string import ascii_lowercase


def missing_alphabets(s):
    c = Counter(s)
    m = max(c.values())
    return ''.join((letter * (m - c[letter]) for letter in ascii_lowercase))
