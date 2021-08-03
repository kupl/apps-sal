from itertools import cycle


def encode(message, key):
    return [ord(a) - 96 + int(b) for a, b in zip(message, cycle(str(key)))]
