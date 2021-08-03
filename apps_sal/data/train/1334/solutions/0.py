import math
n = int(input())
a = list(map(int, input().split()))
dp = [0 for x in range(n)]
dp[0] = a[0]
dp[1] = a[1]
dp[2] = a[2]
for x in range(3, n):
    dp[x] = a[x] + min(dp[x - 1], dp[x - 2], dp[x - 3])

print(min(dp[-3:]))
