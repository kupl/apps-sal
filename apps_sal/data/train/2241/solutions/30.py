import sys
def MI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))


N, C = MI()
A, B = [0] + LI(), [0] + LI()
mod = 10**9 + 7

X = [[0] * 401 for _ in range(401)]
for k in range(401):
    for l in range(1, 401):
        X[k][l] = X[k][l - 1] + pow(l, k, mod)
        X[k][l] %= mod

dp = [[0] * (C + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i in range(1, N + 1):
    a, b = A[i], B[i]
    for j in range(C + 1):
        x = 0
        for k in range(j + 1):
            x += dp[i - 1][j - k] * (X[k][b] - X[k][a - 1])
            x %= mod
        dp[i][j] = x

print((dp[-1][-1]))
