import sys
input = sys.stdin.readline
mod = 10 ** 9 + 7
(N, C) = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
dp = [0] * (C + 1)
dp[0] = 1
for i in range(N):
    X = [0] * (C + 1)
    for j in range(A[i], B[i] + 1):
        x = 1
        for k in range(C + 1):
            X[k] = (X[k] + x) % mod
            x = x * j % mod
    ndp = [0] * (C + 1)
    for j in range(C + 1):
        for k in range(C + 1 - j):
            ndp[j + k] = (ndp[j + k] + dp[j] * X[k]) % mod
    dp = ndp
print(dp[C])
