from functools import reduce
from operator import xor, or_


def disjunction(a, b): return reduce(xor if b else or_, a)
