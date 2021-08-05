def solve():
    MOD = 998244353

    N, K = list(map(int, input().split()))

    N2 = N - N % 2

    dp = [[0] * (N + 1) for _ in range(N - K + 1)]
    accRevDp = [[0] * (N + 1) for _ in range(N - K + 1)]
    dp[0][K] = 1
    accRevDp[0] = [1] * (K + 1) + [0] * (N - K)
    for i in range(1, N - K + 1):
        j = min(N2, 2 * i)
        dp[i][j] = accRevDp[i][j] = accRevDp[i - j // 2][j // 2]
        for j in reversed(list(range(0, min(N2, 2 * i), 2))):
            dp[i][j] = accRevDp[i - j // 2][j // 2]
            accRevDp[i][j + 1] = accRevDp[i][j + 2]
            accRevDp[i][j] = (accRevDp[i][j + 1] + dp[i][j]) % MOD

    ans = sum(dp[N - K]) % MOD
    print(ans)


solve()
