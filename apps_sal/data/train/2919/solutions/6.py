from itertools import cycle

abc = 'abcdefghijklmnopqrstuvwxyz'


def encode(message, key):
    key = cycle(int(x) for x in str(key))
    return [abc.index(m) + 1 + k for m, k in zip(message, key)]
