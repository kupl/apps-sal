import sys
from collections import defaultdict
from copy import copy


def R(t=int):
    return t(input())


def RL(t=int):
    return [t(x) for x in input().split()]


def RLL(n, t=int):
    return [RL(t) for _ in range(n)]


def solve():
    n = R()
    P = RL()
    m = l = P[0]
    for p in P[1:]:
        if l + 1 != p and p > m:
            print('No')
            return
        m = min(m, p)
        l = p
    print('Yes')


T = R()
for _ in range(T):
    solve()
