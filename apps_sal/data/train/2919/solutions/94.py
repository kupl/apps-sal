from itertools import cycle


def encode(message, key):
    return [v + int(v1) for (v, v1) in zip([ord(c) - 96 for c in message], cycle(str(key)))]
