from math import gcd
from functools import reduce
import heapq

def gcd2(xs): return reduce(gcd, xs, xs[0])

def gen(xs):
    seen = set()
    q = list(sorted(xs))
    while True:
        curr = heapq.heappop(q)
        yield curr
        for x in xs:
            t = curr + x
            if t not in seen:
                heapq.heappush(q, t)
                seen.add(t)


def survivor(xs):
    if 1 in xs: return 0
    if not xs or gcd2(xs) > 1: return -1
    i, cnt, m = 0, 1, min(xs)
    g = gen(xs)
    for x in g:
        if x != i + cnt: cnt, i = 1, x
        else: cnt += 1
        if cnt >= m: break
    return i - 1


