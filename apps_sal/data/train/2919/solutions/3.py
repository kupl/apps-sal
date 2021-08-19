import itertools
import string


def encode(message, key):
    return [string.ascii_lowercase.index(c) + k + 1 for (c, k) in zip(message, itertools.cycle((int(c) for c in str(key))))]
