from bisect import bisect_left
from collections import Counter
occ = Counter({0: -1, 1: -1})
for n in range(2, 1000 + 1):
    x = n * n
    while x <= 1000000:
        occ[x] += 1
        x *= n
xs = sorted(occ)


def largest_power(n):
    i = bisect_left(xs, n) - 1
    x = xs[i]
    return (x, occ[x])
