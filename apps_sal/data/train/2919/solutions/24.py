from itertools import cycle


def encode(message, key):
    c = cycle(str(key))
    return [ord(i) + int(ord(next(c))) - 144 for i in message]
