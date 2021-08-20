def main():
    mod = 10 ** 9 + 7
    inv_n = [0] * 1001
    nCr = [[1] * (i + 1) for i in range(1001)]
    for i in range(1001):
        inv_n[i] = pow(i, mod - 2, mod)
    for i in range(2, 1001):
        for j in range(1, i):
            nCr[i][j] = (nCr[i - 1][j - 1] + nCr[i - 1][j]) % mod
    (n, a, b, c, d) = list(map(int, input().split()))
    dp = [0] * (n + 1)
    dp[0] = 1
    for A in range(b, a - 1, -1):
        dp2 = [i for i in dp]
        for N in range(n - c * A, -1, -1):
            e = dp[N]
            if e:
                temp = 1
                for C in range(1, c):
                    temp = temp * nCr[n - N - (C - 1) * A][A] * inv_n[C] % mod
                for C in range(c, min(d, (n - N) // A) + 1):
                    temp = temp * nCr[n - N - (C - 1) * A][A] * inv_n[C] % mod
                    dp2[N + C * A] = (dp2[N + C * A] + temp * e) % mod
        dp = dp2
    print(dp[-1])


main()
