from itertools import combinations
from operator import itemgetter
from bisect import bisect_left
squares = [i * i for i in range(1, 666)]
build = sorted(([x + y >> 1, x - y >> 1] for (y, x) in combinations(squares, 2) if x & 1 == y & 1))
search = list(map(itemgetter(0), build))


def n_closestPairs_tonum(num, k):
    n = bisect_left(search, num) - 1
    return build[n:n - k:-1]
