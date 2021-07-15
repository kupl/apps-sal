from itertools import cycle

def encode(message, key):
    key = cycle(map(int, str(key)))
    return [ord(c)-96+next(key) for c in message]
