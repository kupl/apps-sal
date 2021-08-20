from itertools import cycle


def encode(message, key):
    key = list(map(int, str(key)))
    return [ord(c) - 96 + k for (c, k) in zip(message, cycle(key))]
