n = int(input())
arr = list(map(int, input().split()))
dp = [0] * (n + 1)
dp[0] = 0
dp[1] = arr[0]
dp[2] = arr[0] + arr[1]
dp[3] = max(arr[2] + arr[0], arr[1] + arr[2], dp[-1])
for i in range(4, n + 1):
    dp[i] = max(dp[i - 1], arr[i - 1] + dp[i - 2], arr[i - 1] + arr[i - 2] + dp[i - 3])
print(dp[-1])
