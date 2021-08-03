from math import *
import math


def r1(t):
    return t(input())


def r2(t):
    return [t(i) for i in input().split()]


for zzz in range(r1(int)):
    a, b = r2(int)
    t = min(max(b, 2 * a), max(2 * b, a))
    print(t * t)
