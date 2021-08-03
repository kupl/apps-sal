n = int(input())
ar = list(map(int, input().split()))
dp = [0] * n
dp[0] = ar[0]
dp[1] = ar[1]
for i in range(2, n):
    dp[i] = min(dp[i - 2], dp[i - 1]) + ar[i]

ar.reverse()
# print(ar)
dp1 = [0] * n
dp1[0] = ar[0]
dp1[1] = ar[1]
for i in range(2, n):
    dp1[i] = min(dp1[i - 2], dp1[i - 1]) + ar[i]
print(min(dp[-1], dp1[-1]))
