import math
import string
import itertools
import fractions
import heapq
import collections
import re
import array
import bisect
import sys
import random
import time
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 10
mod = 10 ** 9 + 7


def f():
    (n, t) = list(map(int, input().split()))
    a = list(map(int, input().split()))
    m = 0
    mc = inf
    r = 0
    for c in a:
        if mc > c:
            mc = c
            continue
        if c - mc > m:
            m = c - mc
            r = 1
            continue
        if c - mc == m:
            r += 1
    return r


print(f())
