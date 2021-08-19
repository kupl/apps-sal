from itertools import cycle


def encode(message, key):
    a = []
    for (m, c) in zip(message, cycle(str(key))):
        d = ord(m) - 96 + int(c)
        a.append(d)
    return a
