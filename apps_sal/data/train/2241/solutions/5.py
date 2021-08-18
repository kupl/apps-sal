import sys
N, C = list(map(int, input().split()))
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
mod = 10**9 + 7
table = [[pow(j, i, mod) for j in range(405)] for i in range(405)]
ntable = [[0] * 405 for i in range(405)]
for i in range(405):
    t = 0
    for j in range(1, 405):
        t += table[i][j]
        t %= mod
        ntable[i][j] = t
F = [B[i] - A[i] + 1 for i in range(N)]
G = [0] * N
t = 1
for i in range(N):
    t *= F[i]
    t %= mod
for i in range(N):
    G[i] = (t * pow(F[i], mod - 2, mod)) % mod
dp = [[0] * (C + 1) for i in range(N)]
for i in range(C + 1):
    dp[0][i] = ((ntable[i][B[0]] - ntable[i][A[0] - 1])) % mod
for i in range(1, N):
    for k in range(C + 1):
        for l in range(k + 1):
            dp[i][k] += dp[i - 1][l] * (ntable[k - l][B[i]] - ntable[k - l][A[i] - 1])
            dp[i][k] %= mod
print((dp[N - 1][C]))
