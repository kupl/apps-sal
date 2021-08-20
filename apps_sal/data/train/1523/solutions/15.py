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
        dp = [[0, 0] for x in range(n)]
        if n == 1:
            print(l[0])
        elif n == 2:
            print(sum(l))
        else:
            dp[2][0] = l[2] + l[1]
            dp[2][1] = l[2] + l[0]
            ma = max(dp[1][0], dp[1][1])
            dp[1][1] = l[1]
            dp[1][0] = l[1] + l[0]
            for i in range(3, n):
                dp[i][0] = l[i] + dp[i - 1][1]
                ma = max(dp[i - 2][0], dp[i - 2][1], ma)
                dp[i][1] = ma + l[i]
            ma = 0
            for i in range(n):
                ma = max(dp[i][0], ma, dp[i][1])
            print(ma)
    except:
        pass


M = 998244353
P = 1000000007


def __starting_point():
    for _ in range(1):
        main()


__starting_point()
