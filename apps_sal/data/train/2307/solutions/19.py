n, a, b = map(int, input().split())
x = list(map(int, input().split()))

dp = [float('inf')] * n
dp[0] = 0
for i in range(n - 1):
    dp[i + 1] = dp[i] + min((x[i + 1] - x[i]) * a, b)

print(dp[-1])
