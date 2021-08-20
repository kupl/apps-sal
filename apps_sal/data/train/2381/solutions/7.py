from bisect import bisect_left as bl
from bisect import bisect_right as br
import heapq
import math
from collections import *
from functools import reduce, cmp_to_key
import sys
input = sys.stdin.readline
M = mod = 10 ** 9 + 7


def factors(n):
    return sorted(set(reduce(list.__add__, ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0))))


def inv_mod(n):
    return pow(n, mod - 2, mod)


def li():
    return [int(i) for i in input().rstrip('\n').split()]


def st():
    return input().rstrip('\n')


def val():
    return int(input().rstrip('\n'))


def li2():
    return [i for i in input().rstrip('\n')]


def li3():
    return [int(i) for i in input().rstrip('\n')]


for _ in range(val()):
    s = st()
    n = len(s)
    l = [0 for i in range(n + 2)]
    d = -1
    last = n + 1
    for i in range(len(s), 0, -1):
        if s[i - 1] == 'R':
            l[i] = last - i
            last = i
            d = max(d, l[i])
    d = max(d, last - 0)
    print(d if d > 0 else n + 1)
