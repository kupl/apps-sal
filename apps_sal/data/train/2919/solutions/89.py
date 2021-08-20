from string import ascii_lowercase as abc
from itertools import cycle


def encode(message, key):
    return [int(x) + abc.index(ch) + 1 for (x, ch) in list(zip(cycle(str(key)), message))]
