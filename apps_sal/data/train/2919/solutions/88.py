from string import ascii_lowercase as abc
from itertools import cycle


def encode(message, key):
    return [abc.index(m) + k + 1 for (m, k) in zip(message, cycle(map(int, str(key))))]
