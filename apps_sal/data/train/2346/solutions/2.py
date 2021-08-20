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
    return [i for i in input().rstrip('\n').split(' ')]


def li3():
    return [int(i) for i in input().rstrip('\n')]


for _ in range(val()):
    tot = 0
    (n, d) = li()
    l = li()
    tot = l[0]
    for i in range(1, n):
        while d >= i and l[i]:
            l[i] -= 1
            tot += 1
            d -= i
    print(tot)
