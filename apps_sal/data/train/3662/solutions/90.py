from operator import xor as xor_
from functools import reduce


def xor(a, b):
    return reduce(xor_, (a, b))
