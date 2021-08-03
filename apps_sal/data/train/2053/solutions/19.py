# Bhargey Mehta (Sophomore)
#DA-IICT, Gandhinagar
import sys
import math
import queue
import bisect
#sys.stdin = open("input.txt", "r")
MOD = 10**9 + 7
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
b = sorted(map(int, input().split()))
g = sorted(map(int, input().split()))
if b[n - 1] > g[0]:
    print(-1)
    return
ans = 0
found = False
for i in range(n - 1):
    ans += b[i] * m
ans += sum(g)
for j in range(m):
    if g[j] == b[-1]:
        found = True
if not found:
    ans -= b[-2]
    ans += b[-1]
print(ans)
