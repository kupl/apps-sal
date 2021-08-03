from itertools import accumulate


def nb_year(p0, pct, aug, p):
    return next(i for i, x in enumerate(accumulate([p0] * 1000, lambda px, _: px + .01 * pct * px + aug)) if x >= p)
