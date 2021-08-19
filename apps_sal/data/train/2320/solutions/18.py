from collections import deque
import sys
import math
import string
import bisect
input = sys.stdin.readline


def L():
    return list(map(int, input().split()))


def Ls():
    return list(input().split())


def M():
    return list(map(int, input().split()))


def I():
    return int(input())


n = I()
l = L()
m = L()
x = []
for i in range(n):
    x.append([-m[i], i])
x.sort(key=lambda x: x[0])
x = x[-1::-1]
l.sort(reverse=True)
d = [0] * n
for i in range(n):
    d[x[i][1]] = l[i]
print(*d)
