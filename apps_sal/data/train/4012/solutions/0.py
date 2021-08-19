import numpy as np
from itertools import zip_longest
from string import ascii_lowercase as lower, ascii_uppercase as upper
D = {c: i % 26 for (i, c) in enumerate(lower + upper)}


def encrypt(text, key):
    result = []
    text = ''.join(filter(str.isalpha, text))
    key = np.array(([D[key[0]], D[key[1]]], [D[key[2]], D[key[3]]]))
    for (c1, c2) in zip_longest(text[::2], text[1::2], fillvalue='Z'):
        (x, y) = key @ ([D[c1]], [D[c2]])
        result.append(upper[x[0] % 26] + upper[y[0] % 26])
    return ''.join(result)
