n = int(input())
arr = list(map(int, input().split()))
if(n > 0):
    dp = [0 for i in range(n)]
    dp[0] = arr[0]
    dp[1] = arr[1]
    for i in range(2, n):
        dp[i] = arr[i] + min(dp[i - 1], dp[i - 2])
    comp = (dp[-1])
    dp[1] += dp[0]
    for i in range(2, n - 1):
        dp[i] = arr[i] + min(dp[i - 1], dp[i - 2])
    print(min(comp, dp[n - 2]))
