import sys
import heapq as hq
import itertools
import math
import collections
def ma(): return map(int, input().split())
def lma(): return list(map(int, input().split()))
def tma(): return tuple(map(int, input().split()))
def ni(): return int(input())
def yn(fl): return print("Yes") if fl else print("No")
def ips(): return input().split()


n, t = ma()
A = lma()
INF = 10**15

mns = [INF] * (n + 1)
for i in range(n):
    mns[i] = min(mns[i - 1], A[i])
c = 0
dmx = -1
for i in range(1, n):
    if A[i] - mns[i] > dmx:
        dmx = A[i] - mns[i]
        c = 1
    elif A[i] - mns[i] == dmx:
        c += 1
print(c)
