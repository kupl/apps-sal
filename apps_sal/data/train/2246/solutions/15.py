import sys, math
from heapq import heappush, heappop

readline = sys.stdin.readline
mr = lambda:map(int,readline().split())
n, k = mr()
tmp = list(mr())
a = int(readline())
cost = list(mr())
for i in range(n):
    tmp[i] -= k
buyIndexes = []
energy = 0
ans = 0
for i in range(n):
    heappush(buyIndexes,cost[i])
    if energy < tmp[i]:
        ordered = []
        while energy < tmp[i]:
            energy += a
            if len(buyIndexes) == 0:
                ans = -1
                break
            ans += heappop(buyIndexes)
    if ans == -1:
        break
print(ans)
