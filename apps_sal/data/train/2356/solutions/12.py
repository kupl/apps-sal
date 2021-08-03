N, K = list(map(int, input().split()))
m = 998244353
dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 1
for n in range(1, N + 1):
    for k in range(N, -1, -1):
        if 2 * k <= N:
            dp[n][k] = (dp[n - 1][k - 1] + dp[n][2 * k]) % m
        else:
            dp[n][k] = (dp[n - 1][k - 1]) % m
print((dp[N][K]))
