from functools import reduce
from itertools import chain


def count_find_num(primesL, limit):
    s = [reduce(lambda a, b: a * b, primesL)]
    if s[0] > limit:
        return []
    r = set(s)
    while len(s) > 0:
        s = set(chain.from_iterable(([p * n for p in primesL if p * n <= limit] for n in s)))
        r |= s
    return [len(r), max(r)]
