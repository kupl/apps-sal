# -*- coding: utf-8 -*-
import bisect
import heapq
import math
import random
from collections import Counter, defaultdict, deque
from decimal import ROUND_CEILING, ROUND_HALF_UP, Decimal
from fractions import Fraction
from functools import lru_cache, reduce
from itertools import combinations, combinations_with_replacement, product, permutations, accumulate
from operator import add, mul, sub, itemgetter, attrgetter


import sys
# sys.setrecursionlimit(10**6)
# readline = sys.stdin.buffer.readline
readline = sys.stdin.readline

INF = 1 << 60


def read_int():
    return int(readline())


def read_int_n():
    return list(map(int, readline().split()))


def read_float():
    return float(readline())


def read_float_n():
    return list(map(float, readline().split()))


def read_str():
    return readline().strip()


def read_str_n():
    return readline().strip().split()


def ep(*args):
    print(*args, file=sys.stderr)


def epp(o):
    import pprint
    pprint.pprint(o, stream=sys.stderr)


def gen_2d_array(n, m, fill=0):
    if callable(fill):
        return [[fill()] * m for _ in range(n)]
    else:
        return [[fill] * m for _ in range(n)]


def gen_3d_array(n, m, k, fill=0):
    if callable(fill):
        return [[[fill()] * k for _ in range(m)] for _ in range(n)]
    else:
        return [[[fill] * k for _ in range(m)] for _ in range(n)]


def mt(f):
    import time

    def wrap(*args, **kwargs):
        s = time.perf_counter()
        ret = f(*args, **kwargs)
        e = time.perf_counter()

        ep(e - s, 'sec')
        return ret

    return wrap


@mt
def slv(N, M, A):
    mod = 10**9 + 7
    S = sum(A)
    a = 1
    b = 1
    for i in range(1, N + S + 1):
        a *= i
        a %= mod
        b *= M + N - i + 1
        b %= mod

    return b * pow(a, mod - 2, mod) % mod


def main():
    N, M = read_int_n()
    A = read_int_n()
    print(slv(N, M, A))


def __starting_point():
    main()


__starting_point()
