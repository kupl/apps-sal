from functools import reduce
from operator import xor

def find_missing(xs, ys):
    return reduce(xor, xs, 0) ^ reduce(xor, ys, 0)

