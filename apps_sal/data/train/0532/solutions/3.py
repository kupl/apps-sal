dp = [None] * 1000010
dp[0] = 0
dp[1] = 1
MOD = 15746
n = int(input())
for i in range(2, n + 2):
    dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
print(dp[n + 1])
