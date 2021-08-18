n = 51
dp = [0 for x in range(n)]
for i in range(1, n):
    dp[i] = dp[i - 1] + i * i * i
t = int(input())
for i in range(t):
    num = int(input())
    if num == 1:
        print(1)
    else:
        print(dp[num] + dp[num - 1])
