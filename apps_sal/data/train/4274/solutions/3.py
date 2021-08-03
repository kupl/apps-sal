from itertools import cycle
from functools import reduce


def do_math(stg):
    letters = (c for c in stg if c.isalpha())
    numbers = (float(n) for n in "".join(c for c in stg if not c.isalpha()).split())
    _, numbers = list(zip(*sorted(zip(letters, numbers), key=lambda t: t[0])))
    ops = cycle((float.__add__, float.__sub__, float.__mul__, float.__truediv__))
    return round(reduce(lambda a, b: next(ops)(a, b), numbers))
