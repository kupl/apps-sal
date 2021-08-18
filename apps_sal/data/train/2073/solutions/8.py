'''
    Auther: ghoshashis545 Ashis Ghosh
    College: Jalpaiguri Govt Enggineering College
'''
from os import path
import sys
from functools import cmp_to_key as ctk
from collections import deque, defaultdict as dd
from bisect import bisect, bisect_left, bisect_right, insort, insort_left, insort_right
from itertools import permutations
from datetime import datetime
from math import ceil, sqrt, log, gcd
def ii(): return int(input())
def si(): return input()
def mi(): return list(map(int, input().split()))
def li(): return list(mi())


abc = 'abcdefghijklmnopqrstuvwxyz'
abd = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
mod = 1000000007
inf = float("inf")
vow = ['a', 'e', 'i', 'o', 'u']
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]


def bo(i):
    return ord(i) - ord('a')


def solve():

    n = ii()
    a = li()
    b = []
    for j in range(31, -1, -1):
        for i in range(n):
            if (a[i] >> j) & 1:
                b.append(i)
        if(len(b) < n and len(b) > 0):
            break
        b = []

    if len(b) == n or len(b) == 0:
        print(0)
        return

    ans = 0
    x = 0

    for j in range(len(b) - 1):

        mx = 0
        x1 = a[b[j]]
        for i in range(b[j] - 1, x - 1, -1):
            mx = max(mx, a[i])
            ans = max(ans, x1 ^ mx)
        mx = 0
        for i in range(b[j] + 1, b[j + 1]):
            mx = max(mx, a[i])
            ans = max(ans, x1 ^ mx)
        x = b[j] + 1

    mx = 0
    x1 = a[b[len(b) - 1]]
    for i in range(b[len(b) - 1] - 1, x - 1, -1):
        mx = max(mx, a[i])
        ans = max(ans, x1 ^ mx)

    mx = 0
    for i in range(b[len(b) - 1] + 1, n):
        mx = max(mx, a[i])
        ans = max(ans, x1 ^ mx)

    print(ans)


def __starting_point():

    solve()


__starting_point()
