from math import *
from collections import *
import sys
input = sys.stdin.readline
t = int(input())
while t:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    (p, q) = map(int, input().split())
    s = 0
    a.sort()
    for i in range(n // 2):
        x = a[i]
        x1 = a[n - i - 1]
        if x == p or x1 == p:
            s1 = abs(x - x1)
            s2 = q
            s += abs(atan2(s1, s2))
        elif x < p and x1 > p:
            s1 = abs(p - x)
            ex = atan2(s1, q)
            s1 = abs(p - x1)
            ex1 = atan2(s1, q)
            ex += ex1
            s += abs(ex)
        elif p < x:
            s1 = abs(p - x)
            ex = atan2(s1, q)
            s1 = abs(p - x1)
            ex1 = atan2(s1, q)
            ex = ex1 - ex
            s += abs(ex)
        else:
            s1 = abs(p - x)
            ex = atan2(s1, q)
            s1 = abs(p - x1)
            ex1 = atan2(s1, q)
            ex = ex - ex1
            s += abs(ex)
    print(s)
