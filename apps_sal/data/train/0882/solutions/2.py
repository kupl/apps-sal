from collections import Counter as cc
from sys import stdin as sin


def aint():
    return int(input())


def amap():
    return map(int, sin.readline().split())


def alist():
    return list(map(int, sin.readline().split()))


def astr():
    return input()


for _ in range(int(input())):
    a = input()
    b = input()
    d1 = cc(a)
    d2 = cc(b)
    m = 0
    for i in d1:
        m += min(d1[i], d2[i])
    print(m)
