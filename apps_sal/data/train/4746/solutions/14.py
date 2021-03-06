from functools import reduce


def fisHex(name):
    return reduce(lambda a, b: a ^ b, [int(l, 16) if l in 'abcdef' else 0 for l in name.lower()], 0)
