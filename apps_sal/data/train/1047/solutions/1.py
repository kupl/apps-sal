import io
import sys
import os
import math as ma
from decimal import Decimal as dec
from itertools import permutations


def li():
    return list(map(int, input().split()))


def num():
    return map(int, input().split())


def nu():
    return int(input())


def solve():
    t = nu()
    for _ in range(t):
        n = nu()
        x = set()
        y = set()
        fl = False
        for i in range(n):
            l, r = num()
            px = l + r
            py = r - l
            if(px in x):
                fl = True
            if(py in y):
                fl = True
            x.add(px)
            y.add(py)
        x = list(x)
        y = list(y)
        x.sort()
        y.sort()
        mnx = 9999999999999
        mny = 9999999999999
        if(fl):
            print(0)
        else:
            for i in range(1, len(x)):
                mnx = min(mnx, x[i] - x[i - 1])
            for i in range(1, len(y)):
                mny = min(mny, y[i] - y[i - 1])
            print(min(mny, mnx) / 2)


def __starting_point():
    solve()


__starting_point()
