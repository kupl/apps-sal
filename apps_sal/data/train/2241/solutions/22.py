import sys
from itertools import accumulate
readline = sys.stdin.readline
MOD = 10 ** 9 + 7
(N, C) = map(int, readline().split())
A = [0] + list(map(int, readline().split()))
B = [0] + list(map(int, readline().split()))
acsq = []
lb = max(B) + 1
for j in range(C + 1):
    ac = [0] * lb
    ac[0] = 1
    for i in range(1, lb):
        ac[i] = (ac[i - 1] + pow(i, j, MOD)) % MOD
    acsq.append(ac)
dp = [[0] * (C + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i in range(1, N + 1):
    (a, b) = (A[i], B[i])
    for c in range(C + 1):
        res = 0
        for j in range(c + 1):
            res = (res + (acsq[c - j][b] - acsq[c - j][a - 1]) * dp[i - 1][j]) % MOD
        dp[i][c] = res
print(dp[N][C])
