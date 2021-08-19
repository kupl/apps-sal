dp = [0] * 10000
for i in range(1, 10000):
    dp[i] = dp[i - 1] + i * i
for i in range(int(input())):
    n = int(input())
    print(dp[n - 1])
