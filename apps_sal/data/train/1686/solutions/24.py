MOD = 20011

n, m, d = map(int, input().split())
gr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[1][1] = 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if gr[i - 1][j - 1] == 0:
            dp[i][j] = 0
            continue

        if i == j == 1:
            continue

        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        if i - d - 1 > 0:
            for r in range(i - d - 1, i):
                if not gr[r][j - 1]:
                    break
            else:

                dp[i][j] -= dp[i - d - 1][j]

        if j - d - 1 > 0:
            for r in range(j - d - 1, j):
                if not gr[i - 1][r]:
                    break
            else:
                dp[i][j] -= dp[i][j - d - 1]

        dp[i][j] = max(dp[i][j], 0) % MOD

print(dp[n][m])
