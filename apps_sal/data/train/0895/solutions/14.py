n = int(input())
a = list(map(int, input().split()))
if n == 1:
    print(a[0])
elif n == 2:
    print(min(a[0], a[1]))
else:
    dp = [0] * n
    dp[0] = a[0]
    dp[1] = a[1]
    for i in range(2, n):
        dp[i] = a[i] + min(dp[i - 2], dp[i - 1])
    result1 = dp[n - 1]
    dp = [0] * n
    dp[n - 1] = a[n - 1]
    dp[n - 2] = a[n - 2]
    for i in range(n - 3, -1, -1):
        dp[i] = a[i] + min(dp[i + 2], dp[i + 1])
    result = min(dp[0], result1)
    print(result)
