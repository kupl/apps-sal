import bisect
import collections
import copy
import heapq
import itertools
import math
import string
import sys


def input():
    return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10 ** 7)
INF = float('inf')
MOD = 10 ** 9 + 7


def I():
    return int(input())


def F():
    return float(input())


def SS():
    return input()


def LI():
    return [int(x) for x in input().split()]


def LI_():
    return [int(x) - 1 for x in input().split()]


def LF():
    return [float(x) for x in input().split()]


def LSS():
    return input().split()


def resolve():
    (N, M) = LI()
    G = collections.defaultdict(list)
    for _ in range(M):
        (u, v, c) = LI_()
        G[u].append((v, c))
        G[v].append((u, c))
    ans = [-1] * N
    ans[0] = 1

    def dfs(c, p):
        for (n, l) in G[c]:
            if ans[n] == -1:
                if ans[c] == l:
                    if l < N - 1:
                        ans[n] = l + 1
                    else:
                        ans[n] = l - 1
                else:
                    ans[n] = l
                dfs(n, c)
    dfs(0, -1)
    for i in ans:
        print(i + 1)


def __starting_point():
    resolve()


__starting_point()
