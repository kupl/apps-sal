from collections import defaultdict
import math as mt
import sys
import string
input = sys.stdin.readline


def L():
    return list(map(int, input().split()))


def Ls():
    return list(input().split())


def M():
    return list(map(int, input().split()))


def I():
    return int(input())


t = I()
for _ in range(t):
    n = I()
    l = L()
    v = [0] * n
    a = []
    for i in range(2 * n):
        if v[l[i] - 1] == 0:
            a.append(l[i])
            v[l[i] - 1] = 1
    print(*a)
