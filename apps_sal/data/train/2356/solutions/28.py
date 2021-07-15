def solve():
    MOD = 998244353

    N, K = list(map(int, input().split()))

    dp = [[0]*(N+1) for _ in range(N+1)]
    dp[0][0] = 1
    for num in range(1, N+1):
        for sm in reversed(list(range(N+1))):
            if num > 0 and sm > 0:
                dp[num][sm] += dp[num-1][sm-1]
            if 2*sm <= N:
                dp[num][sm] += dp[num][2*sm]
            dp[num][sm] %= MOD

    ans = dp[N][K]
    print(ans)


solve()

