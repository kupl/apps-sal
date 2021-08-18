import sys
input = sys.stdin.readline


def power_func(a, n, mod):
    bi = str(format(n, "b"))
    res = 1
    for i in range(len(bi)):
        res = (res * res) % mod
        if bi[i] == "1":
            res = (res * a) % mod
    return res


def main():
    N, C = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    mod = 10**9 + 7
    L = 400

    dp = [[0] * (L + 1) for _ in range(C + 1)]
    count = B[0] - A[0] + 1
    for c in range(C + 1):
        a, b = A[0], B[0]
        dp[c][0] = power_func(a, c, mod)
        for k in range(1, b - a + 1):
            dp[c][k] = (dp[c][k - 1] + power_func(a + k, c, mod)) % mod
        dp[c][L] = dp[c][b - a]

    for i, (a, b) in enumerate(zip(A, B)):
        if i == 0:
            continue
        for k in range(b - a + 1):
            dp[0][k] = count * (k + 1) % mod
        dp[0][L] = dp[0][b - a]
        for c in range(1, C + 1):
            dp[c][0] = (dp[c][L] + a * dp[c - 1][0]) % mod
            for k in range(1, b - a + 1):
                R = dp[c][k - 1] + dp[c][L] + (a + k) * (dp[c - 1][k] - dp[c - 1][k - 1])
                if R < 0:
                    R += mod
                dp[c][k] = R % mod
            dp[c][L] = dp[c][b - a]
        count = (count * (b - a + 1)) % mod

    print(dp[C][L])


def __starting_point():
    main()


__starting_point()
