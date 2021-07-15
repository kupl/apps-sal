import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

XY = [(a, i) for i, a in enumerate(A)]
XY.sort(reverse=True)

# 解説
ans = [0] * N
min_y = IINF
for i, (x, y) in enumerate(XY):
    min_y = min(min_y, y)
    x2 = XY[i + 1][0] if i + 1 < N else 0
    ans[min_y] += (x - x2) * (i + 1)
print(*ans, sep='\n')

