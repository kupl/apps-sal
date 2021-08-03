from functools import lru_cache
import sys
3


MOD = 1000000007

cnk = [[1 for i in range(1001)] for j in range(1001)]
for i in range(1, 1001):
    for j in range(1, i):
        cnk[i][j] = cnk[i - 1][j - 1] + cnk[i - 1][j]


k = int(input())
cs = [int(input()) for i in range(k)]

ans = 1
sm = 0
for c in cs:
    sm += c
    ans = (ans * cnk[sm - 1][c - 1]) % MOD

print(ans)
