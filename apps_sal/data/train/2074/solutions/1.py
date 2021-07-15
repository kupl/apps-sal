def solve(n, k, As):
    As.sort()
    m, r = divmod(n, k)
    dp = [0] * (r + 1)
    for i in range(1, k):
        im = i * m
        new_dp = [0] * (r + 1)
        new_dp[0] = dp[0] + As[im] - As[im - 1]
        for h in range(1, min(i, r) + 1):
            new_dp[h] = max(dp[h], dp[h - 1]) + As[im + h] - As[im + h - 1]
        dp = new_dp
    return As[-1] - As[0] - max(dp[r], dp[r-1])

n, k = map(int, input().split())
As = list(map(int, input().split()))
print(solve(n, k, As))
