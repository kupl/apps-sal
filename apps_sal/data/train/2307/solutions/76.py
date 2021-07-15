#coding: utf-8
N, A, B = list(map(int, input().split()))
X = list(map(int, input().split()))
dp = [float("inf") for _ in range(N)]
dp[0] = 0
for i in range(1, N):
    dp[i] = min(A * (X[i] - X[i-1]), B, dp[i]) + dp[i-1]
print((dp[N-1]))

