from itertools import cycle
def encode(message, key):
    a = cycle(str(key))
    return [(ord(x)-96) + int(next(a)) for x in message]

