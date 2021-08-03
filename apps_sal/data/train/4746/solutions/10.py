from operator import xor
from functools import reduce


def fisHex(name):
    return reduce(xor, (ord(c) - 87 for c in name.lower() if c in "abcdef"), 0)
