from itertools import tee


def is_alt(s):
    (xs1, xs2) = tee(map(lambda x: x in 'aeiou', s))
    next(xs2)
    return all((a != b for (a, b) in zip(xs1, xs2)))
