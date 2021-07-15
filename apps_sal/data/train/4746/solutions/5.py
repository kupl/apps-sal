from functools import reduce
from operator import xor

def fisHex(name):
    return reduce(xor, (int(x, 16) for x in name.lower() if 'a' <= x <= 'f'), 0)
