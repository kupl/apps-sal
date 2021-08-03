n, c = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ab = list(zip(a, b))
table = [[0 for i in range(c + 1)] for j in range(401)]
mod = 10**9 + 7
for j in range(c + 1):
    if j == 0:
        for i in range(401):
            table[i][j] = 1
    else:
        for i in range(401):
            table[i][j] = table[i][j - 1] * i % mod
dp = [[0 for i in range(c + 1)] for j in range(n + 1)]
for i in range(c + 1):
    dp[0][i] = 1
for i in range(1, n + 1):
    a, b = ab[i - 1]
    for j in range(a, b + 1):
        for k in range(c + 1):
            dp[i][k] = (dp[i][k] + table[j][k]) % mod
ans = [[0 for i in range(c + 1)] for j in range(n + 1)]
ans[0][0] = 1
for i in range(1, n + 1):
    for j in range(c + 1):
        for k in range(j + 1):
            ans[i][j] = (ans[i][j] + dp[i][k] * ans[i - 1][j - k]) % mod
print(ans[n][c])
