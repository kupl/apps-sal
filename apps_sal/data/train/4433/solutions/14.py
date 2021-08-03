from operator import and_, or_, xor
from functools import reduce


def logical_calc(xs, op): return reduce({'AND': and_, 'OR': or_, 'XOR': xor}.get(op), xs)
