

n, k1, *l = map(int, input().split())
v_l, b_l = l[:n], l[n:]

for i in range(n):
    b_l[i] -= 1

dp = [[0 for _ in range(n)] for _ in range(n)]
for k in range(1, n):
    for j in range(n - 2, -1, -1):
        if j + k >= n:
            continue
        elif b_l[j + k] - k1 == b_l[j]:
            if j + k - 1 < n:
                dp[j][j + k] = max(dp[j][j + k], v_l[j + k] + v_l[j] + dp[j + 1][j + k - 1])
            else:
                dp[j][j + k] = max(dp[j][j + k], v_l[j + k] + v_l[j])
        for i in range(j, j + k):
            dp[j][j + k] = max(dp[j][j + k], dp[j][i] + dp[i + 1][j + k])

print(dp[0][-1])
