# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
import sys
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations
from operator import add, mul, sub

input = sys.stdin.readline

sys.setrecursionlimit(100000)


def read_int():
    return int(input())


def read_int_n():
    return list(map(int, input().split()))


def read_float():
    return float(input())


def read_float_n():
    return list(map(float, input().split()))


def read_str():
    return input().strip()


def read_str_n():
    return list(map(str, input().split()))


def error_print(*args):
    print(*args, file=sys.stderr)


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.time()
        ret = f(*args, **kwargs)
        e = time.time()

        error_print(e - s, 'sec')
        return ret

    return wrap


@mt
def slv(N, Q, STX, D):
    E = []
    for i, (s, t, x) in enumerate(STX):
        E.append((s - x, 1, x, i))
        E.append((t - x, -1, x, i))
    E.sort(reverse=True)

    q = []
    done = set()
    ans = [-1] * Q
    for j, d in enumerate(D):
        while E and E[-1][0] <= d:
            t, e, x, i = E.pop()
            if e == 1:
                heapq.heappush(q, (x, i))
            else:
                done.add((x, i))

        while q and q[0] in done:
            done.remove(heapq.heappop(q))

        if q:
            ans[j] = q[0][0]

    for i in range(Q):
        print(ans[i])


def main():
    N, Q = read_int_n()
    STX = list(read_int_n() for _ in range(N))
    D = list(read_int() for _ in range(Q))
    (slv(N, Q, STX, D))


def __starting_point():
    main()


__starting_point()
