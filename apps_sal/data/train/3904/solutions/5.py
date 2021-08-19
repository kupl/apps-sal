from itertools import product
from string import digits


def iter_candidates(s, pos):
    xs = list(s)
    for ds in product(digits, repeat=len(pos)):
        for (i, d) in zip(pos, ds):
            xs[i] = d
        yield ''.join(xs)


def is_divisible_by_6(s):
    pos = [i for (i, x) in enumerate(s) if x == '*']
    return [x for x in iter_candidates(s, pos) if int(x) % 6 == 0]
