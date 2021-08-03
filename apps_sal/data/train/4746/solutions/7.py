from operator import xor
from functools import reduce


def fisHex(name):
    return reduce(xor, [int(x, 16) for x in name.lower() if x in 'abcdef'], 0)
