import math

mod = 10**9 + 7


def main():
    N, K = list(map(int, input().split()))
    dp = [1] * (K + 1)
    for j in range(1, N):
        val = 1
        for i in range(1, K + 1):
            dp[i] = (dp[i - 1] + dp[i]) % mod
    print(dp[K])


def __starting_point():
    main()


__starting_point()
