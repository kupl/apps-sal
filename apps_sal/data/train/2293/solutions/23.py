def max2(a, b, c, d):
    vals = sorted((a, b, c, d), reverse=True)
    return (vals[0], vals[1])


n = int(input())
a = list(map(int, input().split()))
dp = [[0] * (1 << n) for i in range(n + 1)]
dq = [[0] * (1 << n) for i in range(n + 1)]
for i in range(1 << n):
    dp[0][i] = a[i]
for i in range(n):
    for bit_state in range(1 << n):
        if 1 << i & bit_state:
            (first, second) = max2(dp[i][bit_state], dq[i][bit_state], dp[i][bit_state ^ 1 << i], dq[i][bit_state ^ 1 << i])
        else:
            (first, second) = (dp[i][bit_state], dq[i][bit_state])
        (dp[i + 1][bit_state], dq[i + 1][bit_state]) = (first, second)
ans = 0
for i in range(1, 1 << n):
    ans = max(ans, dp[-1][i] + dq[-1][i])
    print(ans)
