from string import ascii_lowercase as abc
from itertools import cycle


def encode(message, key):
    ch_idx = [abc.index(ch) + 1 for ch in message]
    return [int(x) + y for (x, y) in list(zip(cycle(str(key)), ch_idx))]
