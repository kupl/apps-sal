import bisect
import copy
import heapq
import math
import sys
from collections import *
from functools import lru_cache
from itertools import accumulate, combinations, permutations, product


def input():
    return sys.stdin.readline()[:-1]


def ruiseki(lst):
    return [0] + list(accumulate(lst))


def celi(a, b):
    return -(-a // b)


sys.setrecursionlimit(5000000)
mod = pow(10, 9) + 7
al = [chr(ord('a') + i) for i in range(26)]
direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
(s, t) = (input(), input())
q = int(input())
abcd = [list(map(int, input().split())) for i in range(q)]
scnt = [(0, 0)] * (len(s) + 1)
tcnt = [(0, 0)] * (len(t) + 1)
for i in range(len(s)):
    (a, b) = scnt[i]
    if s[i] == 'A':
        a += 1
    else:
        b += 1
    scnt[i + 1] = (a, b)
for i in range(len(t)):
    (a, b) = tcnt[i]
    if t[i] == 'A':
        a += 1
    else:
        b += 1
    tcnt[i + 1] = (a, b)
for i in range(q):
    (a, b, c, d) = abcd[i]
    (sa, sb) = (scnt[b], scnt[a - 1])
    (sa, sb) = (sa[0] - sb[0], sa[1] - sb[1])
    (ta, tb) = (tcnt[d], tcnt[c - 1])
    (ta, tb) = (ta[0] - tb[0], ta[1] - tb[1])
    if abs(sa - sb - (ta - tb)) % 3 == 0:
        print('YES')
    else:
        print('NO')
