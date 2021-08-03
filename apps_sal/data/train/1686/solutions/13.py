MOD = 20011

n, m, d = map(int, input().split())
gr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]

for i in range(min(n, d + 1)):
    if gr[i][0] == 0:
        break

    dp[i][0] = 1

for i in range(min(m, d + 1)):
    if gr[0][i] == 0:
        break

    dp[0][i] = 1

for i in range(1, n):
    for j in range(1, m):
        if gr[i][j] == 0:
            dp[i][j] = 0
            continue

        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        if i - d - 1 >= 0:
            for r in range(i - d, i):
                if not gr[r][j]:
                    break
            else:
                dp[i][j] -= dp[i - d - 1][j]

                if i - d - 2 >= 0:
                    dp[i][j] += dp[i - d - 2][j]

        if j - d - 1 >= 0:
            for r in range(j - d, j):
                if not gr[i][r]:
                    break
            else:
                dp[i][j] -= dp[i][j - d - 1]

                if j - d - 2 >= 0:
                    dp[i][j] += dp[i][j - d - 2]

        dp[i][j] = max(dp[i][j], 0) % MOD

print(dp[n - 1][m - 1])
