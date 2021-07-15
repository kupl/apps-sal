import math
n = int(input())
a = [int(i) for i in input().split()]
dp = [0 for i in range(n)]
dp[0] = a[0]
dp[1] = a[1]
dp[2] = a[2]
for i in range(3,n):
    dp[i] = a[i] + min(dp[i-1],dp[i-2],dp[i-3])
ans = min(dp[-3:])
print(ans)
