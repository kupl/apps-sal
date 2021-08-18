import typing
import sys
import math
import collections
import bisect
import itertools
import heapq
import decimal
import copy
import operator

INF = 10 ** 20
MOD = 10 ** 9 + 7


def ni(): return int(sys.stdin.readline())
def ns(): return list(map(int, sys.stdin.readline().split()))
def na(): return list(map(int, sys.stdin.readline().split()))
def na1(): return list([int(x) - 1 for x in sys.stdin.readline().split()])


def main():
    s = input()

    if s[0] == "0" or s[-1] == "1":
        print((-1))
        return()

    s = s[:-1]
    n = len(s)
    for i in range(n):
        if s[i] != s[n - 1 - i]:
            print((-1))
            return

    pool = []
    idx = 0
    for i in range(1, n):
        if s[i] == "1":
            print((idx + 1, i + 1))
            idx = i
            for pi in pool:
                print((idx + 1, pi + 1))
            pool = []
        else:
            pool.append(i)
    print((n, n + 1))


def __starting_point():
    main()


__starting_point()
