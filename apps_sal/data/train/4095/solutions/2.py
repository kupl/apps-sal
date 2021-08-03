from functools import reduce
from operator import xor


def added_char(s1, s2):
    return chr(reduce(xor, map(ord, s1), 0) ^ reduce(xor, map(ord, s2), 0))
