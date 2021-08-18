from itertools import accumulate, combinations, permutations
from heapq import heapify, heappop, heappush
from functools import lru_cache
from collections import Counter
from bisect import bisect_left, bisect, bisect_right
from decimal import Decimal
from collections import deque
from operator import itemgetter
from copy import deepcopy as dcp
from copy import copy, deepcopy
import math
import sys
sys.setrecursionlimit(10**7)


def input():
    x = sys.stdin.readline()
    return x[:-1] if x[-1] == "\n" else x


def printl(li): _ = print(*li, sep="\n") if li else None


def argsort(s, return_sorted=False):
    inds = sorted(range(len(s)), key=lambda k: s[k])
    if return_sorted:
        return inds, [s[i] for i in inds]
    return inds


def alp2num(c, cap=False): return ord(c) - 97 if not cap else ord(c) - 65
def num2alp(i, cap=False): return chr(i + 97) if not cap else chr(i + 65)


def matmat(A, B):
    K, N, M = len(B), len(A), len(B[0])
    return [[sum([(A[i][k] * B[k][j]) for k in range(K)]) for j in range(M)] for i in range(N)]


def matvec(M, v):
    N, size = len(v), len(M)
    return [sum([M[i][j] * v[j] for j in range(N)]) for i in range(size)]


def T(M):
    n, m = len(M), len(M[0])
    return [[M[j][i] for j in range(n)] for i in range(m)]


def main():
    mod = 1000000007

    s = input()
    N = len(s)
    f = 1
    if s[-1] == "1" or s[0] == "0":
        f = 0
    for i in range(1, N // 2 + 1):
        if s[i - 1] != s[N - i - 1]:
            f = 0
            break
    if not f:
        print(-1)
        return

    il = []
    edge = []
    for i in range(1, N // 2 + 1):
        if s[i - 1] == "0":
            il.append(i)
        else:
            for j in il:
                edge.append((i, j))
            il = [i]
    i = N // 2 + 1
    for j in il:
        edge.append((i, j))
    j = i
    for i in range(N // 2 + 2, N + 1):
        edge.append((j, i))

    for e in edge:
        print(*e)


def __starting_point():
    main()


__starting_point()
