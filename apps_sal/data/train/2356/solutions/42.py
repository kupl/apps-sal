N, K = list(map(int, input().split()))

MOD = 998244353

dp = [[0 for i in range(N + 1)] for j in range(N + 1)]

dp[1][1] = 1

for i in range(1, N + 1):
    for j in range(N, 0, -1):
        if (i, j) == (1, 1):
            continue
        else:
            dp[i][j] = (dp[i - 1][j - 1] + (dp[i][2 * j] if 2 * j <= N else 0)) % MOD

print((dp[N][K]))
