t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    dp = [-1] * (n + 1)
    dp[0] = 0

    for k in l:
        even = dp[0]
        odd = dp[k]
        dp[k] = max(odd, even + 1)
        dp[0] = max(even, odd + 1)
    print(n - dp[0])
