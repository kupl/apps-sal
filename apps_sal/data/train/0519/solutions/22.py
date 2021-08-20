inpu = list(map(int, input().split()))
(n, k) = (inpu[0], inpu[1])
v = inpu[2:n + 2]
b = inpu[n + 2:2 * n + 2]
dp = [[0 for i in range(n)] for j in range(n)]
for j in range(1, n):
    for i in range(n - j):
        ans = -float('inf')
        if b[i + j] - b[i] == k:
            if j == 1:
                ans = max(ans, v[i + j] + v[i])
            else:
                ans = max(ans, v[i + j] + v[i] + dp[i + 1][i + j - 1])
        for l in range(i + 1, i + j):
            if b[l] - b[i] == k:
                if l == i + 1:
                    ans = max(ans, v[l] + v[i] + dp[l + 1][i + j])
                else:
                    ans = max(ans, v[l] + v[i] + dp[l + 1][i + j] + dp[i + 1][l - 1])
        ans = max(ans, dp[i + 1][i + j])
        dp[i][i + j] = ans
print(dp[0][n - 1])
