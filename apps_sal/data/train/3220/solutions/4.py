from itertools import groupby
from operator import itemgetter


def solve(a, b):

    def factors(n):
        seen = set([1, n])
        for a in range(2, 1 + int(n ** 0.5)):
            (b, m) = divmod(n, a)
            if m == 0:
                if a in seen:
                    break
                seen.add(a)
                seen.add(b)
        return seen
    s = 0
    for (k, g) in groupby(sorted(((sum(factors(a)) / a, a) for a in range(a, b)), key=itemgetter(0)), key=itemgetter(0)):
        gl = list(g)
        if len(gl) > 1:
            s += min(map(itemgetter(1), gl))
    return s
