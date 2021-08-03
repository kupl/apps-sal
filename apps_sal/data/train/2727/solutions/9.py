from string import ascii_lowercase
from collections import Counter


def missing_alphabets(s):
    C = Counter(s)
    x = C.most_common(1)[0][1]
    return ''.join(c * (x - C[c]) for c in ascii_lowercase)
