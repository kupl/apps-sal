from itertools import combinations
P = 998244353
nn = 2002002
fa = [1] * (nn + 1)
fainv = [1] * (nn + 1)
for i in range(nn):
    fa[i + 1] = fa[i] * (i + 1) % P
dp = []
for _ in range(3001):
    dp.append([0] * 3001)
for i in range(3001):
    dp[i][i] = 1
for i in range(1, 3001):
    for j in reversed(range(1, i)):
        if 2 * j > 3000:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = (dp[i - 1][j - 1] + dp[i][2 * j]) % P
(N, K) = [int(i) for i in input().split()]
print(dp[N][K])
