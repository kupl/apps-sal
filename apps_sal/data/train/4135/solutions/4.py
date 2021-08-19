from collections import Counter


def solve(stg):
    c = tuple(Counter(stg).values())
    (mn, mx) = (min(c), max(c))
    (l, cmx) = (len(c), c.count(mx))
    return 1 in (l, mx) or mx - mn == cmx == 1 or l - cmx == mn == 1
