size = 10**4 + 1
dp = [0 for x in range(size)]
for i in range(1, size):
    dp[i] = dp[i - 1] + i * i
t = int(input())
for i in range(t):
    num = int(input())
    print(dp[num - 1])
