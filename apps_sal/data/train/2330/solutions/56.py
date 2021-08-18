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

sys.setrecursionlimit(100000)
input = sys.stdin.readline
INF = 2**62 - 1


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
def slv(S):
    N = len(S)
    if S[N - 1] == '1':
        print(-1)
        return -1

    if S[0] != '1':
        print(-1)
        return -1

    if S[N - 2] != '1':
        print(-1)
        return -1

    for i in range(N // 2):
        if S[i] != S[N - 2 - i]:
            print(-1)
            return -1

    p = [N]
    for i in range(N, 0, -1):
        if S[i - 1] == '1':
            p.append(i)
        else:
            p.append(p[-1])
    p.reverse()
    e = []
    for i in range(1, N):
        e.append((i, p[i]))

    for u, v in e:
        print(u, v)


def main():
    S = read_str()
    (slv(S))


def __starting_point():
    main()


__starting_point()
