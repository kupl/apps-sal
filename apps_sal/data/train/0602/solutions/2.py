from math import inf
from sys import stdin
input = stdin.readline
a = input().split()
mi = inf
ind = 0
n = len(a)
for i in range(n):
    if mi > len(a[i]):
        mi = len(a[i])
        ind = i
for i in range(n):
    print(a[ind], a[i], end=" ")
print(a[ind])
