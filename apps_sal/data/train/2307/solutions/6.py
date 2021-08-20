def main():
    (N, A, B) = map(int, input().split())
    X = list(map(int, input().split()))
    dp = [float('inf')] * (N + 5)
    dp[0] = 0
    for i in range(1, N):
        dp[i] = dp[i - 1] + min((X[i] - X[i - 1]) * A, B)
    print(dp[N - 1])


def __starting_point():
    main()


__starting_point()
