# coding: utf-8
# Your code here!
import sys
read = sys.stdin.read
readline = sys.stdin.readline

n, c = list(map(int, readline().split()))
*a, = list(map(int, readline().split()))
*b, = list(map(int, readline().split()))

M = 401
MOD = 10**9 + 7

powsum = []
for i in range(M):
    res = [pow(j, i, MOD) for j in range(M)]
    for j in range(1, M):
        res[j] = (res[j] + res[j - 1]) % MOD
    powsum.append(res)

dp = [0] * (c + 1)  # dp[i][k] = i まで見て k次斉次式
dp[0] = 1

for ai, bi in zip(a, b):
    ndp = [0] * (c + 1)
    for k in range(c + 1):
        for j in range(k + 1):
            ndp[k] += (powsum[j][bi] - powsum[j][ai - 1]) * dp[k - j] % MOD
        ndp[k] %= MOD

    dp = ndp

print((dp[c] % MOD))
