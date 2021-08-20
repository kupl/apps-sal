from math import *
import math


def r1(t):
    return t(input())


def r2(t):
    return [t(i) for i in input().split()]


def r3(t):
    return [t(i) for i in input()]


for zzz in range(r1(int)):
    n = r1(int)
    g = []
    for i in range(n):
        g.append(r3(int))
    ha = True
    for i in range(n - 1):
        for j in range(n - 1):
            if g[i][j] and (not g[i][j + 1]) and (not g[i + 1][j]):
                ha = False
                break
        if not ha:
            break
    if ha:
        print('YES')
    else:
        print('NO')
