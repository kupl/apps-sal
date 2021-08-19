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
import copy
import functools
sys.setrecursionlimit(10 ** 7)
inf = 10 ** 20
eps = 1.0 / 10 ** 10
mod = 10 ** 9 + 7
dd = [(-1, 0), (0, 1), (1, 0), (0, -1)]
ddn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def LI():
    return [int(x) for x in sys.stdin.readline().split()]


def LI_():
    return [int(x) - 1 for x in sys.stdin.readline().split()]


def LF():
    return [float(x) for x in sys.stdin.readline().split()]


def LS():
    return sys.stdin.readline().split()


def I():
    return int(sys.stdin.readline())


def F():
    return float(sys.stdin.readline())


def S():
    return input()


def pf(s):
    return print(s, flush=True)


def main():
    n = I()
    n2 = 2 ** n
    a = LI()
    t = [[0, 0] for _ in range(n2)]
    ii = [2 ** i for i in range(18)]
    M = n2
    for i in range(n2):
        ti = t[i]
        ti[0] = a[i] * M + i
        for j in range(18):
            if not i & ii[j]:
                continue
            for c in t[i ^ ii[j]]:
                if ti[0] < c:
                    ti[1] = ti[0]
                    ti[0] = c
                elif ti[1] < c and ti[0] != c:
                    ti[1] = c
    r = [0]
    for i in range(1, n2):
        tr = sum(map(lambda x: x // M, t[i]))
        if tr > r[-1]:
            r.append(tr)
        else:
            r.append(r[-1])
    return '\n'.join(map(str, r[1:]))


print(main())
