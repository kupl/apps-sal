from bisect import bisect_left
from sys import stdin
n = int(stdin.readline())
l = []
for i in range(n):
    t = int(stdin.readline())
    l.append(t)
    l.sort()
    print(i + 1 - bisect_left(l, t))
