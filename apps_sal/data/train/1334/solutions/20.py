from sys import stdin, stdout
import math
import sys
import heapq
from itertools import permutations, combinations
from collections import defaultdict, deque, OrderedDict
from os import path
import random
import bisect as bi


def yes():
    print('YES')


def no():
    print('NO')


if path.exists('input.txt'):
    sys.stdin = open('input.txt', 'r')
    sys.stdout = open('output.txt', 'w')

    def I():
        return int(input())

    def In():
        return map(int, input().split())
else:

    def I():
        return int(stdin.readline())

    def In():
        return map(int, stdin.readline().split())


def dict(a):
    d = {}
    for x in a:
        if d.get(x, -1) != -1:
            d[x] += 1
        else:
            d[x] = 1
    return d


def find_gt(a, x):
    """Find leftmost value greater than x"""
    i = bi.bisect_left(a, x)
    if i != len(a):
        return i
    else:
        return -1


def main():
    try:
        n = I()
        l = list(In())
        dp = [0 for x in range(n)]
        for x in range(n):
            if x < 3:
                dp[x] = l[x]
            else:
                dp[x] = min(dp[x - 1], dp[x - 2], dp[x - 3]) + l[x]
        print(min(dp[-1], dp[-2], dp[-3]))
    except:
        pass


M = 998244353
P = 1000000007


def __starting_point():
    for _ in range(1):
        main()


__starting_point()
