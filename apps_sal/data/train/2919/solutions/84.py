from itertools import cycle


def encode(message, key):
    return [ord(c) - 96 + int(k) for (c, k) in zip(message, cycle(str(key)))]
