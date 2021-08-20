from itertools import cycle
from string import ascii_lowercase


def decode(code, key):
    keys = cycle(map(int, str(key)))
    return ''.join((ascii_lowercase[n - next(keys) - 1] for n in code))
