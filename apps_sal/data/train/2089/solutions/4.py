# -*- coding: utf-8 -*-

import math
import collections
import bisect
import heapq
import time
import random
import itertools
import sys

"""
created by shhuan at 2017/11/5 16:54

"""

N = int(input())

P = []
for i in range(N):
    P.append(input().split())


N = 2
S = [0, 1023]
T = [v for v in S]
for i in range(N):
    for p, v in P:
        v = int(v)
        if p == '^':
            T[i] ^= v
        elif p == '|':
            T[i] |= v
        else:
            T[i] &= v

a, b, c = 0, 0, 0
for i in range(10, -1, -1):
    a <<= 1
    b <<= 1
    c <<= 1
    c |= 1
    if all([(v >> i) & 1 == 1for v in T]):
        b |= 1
    elif all([(v >> i) & 1 == 0 for v in T]):
        c >>= 1
        c <<= 1
    elif all([(S[j] >> i) & 1 != (T[j] >> i) & 1 for j in range(N)]):
        a |= 1


print(3)
print('^', a)
print('|', b)
print('&', c)
