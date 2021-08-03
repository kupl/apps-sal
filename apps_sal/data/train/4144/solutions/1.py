from operator import itemgetter
from bisect import bisect

LIMIT = 2000

memo, result = [0] * LIMIT, {}
for x in range(1, LIMIT):
    if memo[x] > x:
        result[x] = memo[x] - x
    if x < LIMIT // 2:
        for y in range(x, LIMIT, x):
            memo[y] += x
values = list(result.keys())


def abundant(h):
    x = values[bisect(values, h) - 1]
    return [[x], [result[x]]]
