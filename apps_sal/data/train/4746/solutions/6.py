from functools import reduce
from operator import xor

def fisHex(name):
    s = set("abcdef")
    return reduce(xor, map(lambda c: int(c,16), (c for c in name.lower() if c in s)),0)
