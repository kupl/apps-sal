import math
import string
import itertools
import collections
import re
import fractions
import array
import copy
import bisect
import heapq
from itertools import chain, dropwhile, permutations, combinations
from collections import deque, defaultdict, OrderedDict, namedtuple, Counter, ChainMap


def VI():
    return list(map(int, input().split()))


def I():
    return int(input())


def LIST(n, m=None):
    return [0] * n if m is None else [[0] * m for i in range(n)]


def ELIST(n):
    return [[] for i in range(n)]


def MI(n=None, m=None):
    if n is None:
        (n, m) = VI()
    arr = LIST(n)
    for i in range(n):
        arr[i] = VI()
    return arr


def MS(n=None, m=None):
    if n is None:
        (n, m) = VI()
    arr = LIST(n)
    for i in range(n):
        arr[i] = input()
    return arr


def MIT(n=None, m=None):
    if n is None:
        (n, m) = VI()
    a = MI(n, m)
    arr = LIST(m, n)
    for (i, l) in enumerate(a):
        for (j, x) in enumerate(l):
            arr[j][i] = x
    return arr


def main(info=0):
    (l, r) = VI()
    if l == r:
        print(l)
        return
    print(2)


def __starting_point():
    main()


__starting_point()
