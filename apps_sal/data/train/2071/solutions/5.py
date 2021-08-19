import collections
import itertools
import functools
import math


def solve():
    n = int(input())
    p = [tuple(map(int, input().split())) for _ in range(n)]
    cnt = collections.Counter((x for (x, _) in p))
    cnt2 = collections.Counter((y for (_, y) in p))
    cntp = collections.Counter(p)
    r = 0
    for (k, v) in cnt.most_common() + cnt2.most_common():
        r += v * (v - 1)
    for (k, v) in cntp.most_common():
        r -= v * (v - 1)
    return r // 2


def __starting_point():
    print(solve())


__starting_point()
