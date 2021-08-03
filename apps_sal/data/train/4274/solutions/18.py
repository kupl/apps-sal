from functools import reduce
from itertools import cycle
from operator import *


def do_math(s):
    n = []
    for w in s.split():
        a, b = '', ''
        for c in w:
            if c.isdigit():
                a += c
            else:
                b += c
        n += [(b, int(a))]
    ops = cycle([add, sub, mul, truediv])
    return round(reduce(lambda *a: next(ops)(*a), [v for c, v in sorted(n, key=lambda x:x[0])]))
