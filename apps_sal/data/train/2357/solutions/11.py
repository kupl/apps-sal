import bisect
import functools
import heapq
import itertools
import sys
import math
import random
import time
from collections import Counter, deque, defaultdict
from functools import reduce
from operator import xor, itemgetter
from pprint import pprint
from types import FunctionType
from typing import List, Any
from sys import stdin
mod = 10 ** 9 + 7
sys.setrecursionlimit(10 ** 9)


def inp():
    return stdin.readline().rstrip()


def lmi():
    return list(map(int, stdin.readline().split()))


def narray(*shape, init: Any = 0):
    if shape:
        return [narray(*shape[1:], init=init) for _ in range(shape[0])]
    if callable(init):
        return init()
    return init


def comb(N, k):
    if k > N or N < 0 or k < 0:
        return 0
    (N, k) = list(map(int, (N, k)))
    top = N
    val = 1
    while top > N - k:
        val *= top
        top -= 1
    n = 1
    while n < k + 1:
        val //= n
        n += 1
    return val


def cmb(x, y):
    if x < y:
        return 0
    bunsi = 1
    bunbo = 1
    for i in range(1, y + 1):
        bunsi = bunsi * (x + 1 - i) % mod
        bunbo = bunbo * i % mod
    res = bunsi * pow(bunbo, mod - 2, mod) % mod
    return res


def main():
    (N, M) = lmi()
    A = lmi()
    ans = cmb((M + N) % mod, (N + sum(A)) % mod) % mod
    print(ans)


def __starting_point():
    main()


__starting_point()
