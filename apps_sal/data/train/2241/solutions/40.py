def main1(n, c, a, b):
    mod = 10**9 + 7
    dp = [[0] * (c + 1) for i in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        ary = [0] * (b[i] + 1 - a[i])
        tmp = 0
        for j in range(c + 1):
            tmp += dp[i][j] * (b[i] + 1 - a[i])
            tmp %= mod
            dp[i + 1][j] += tmp
            dp[i + 1][j] %= mod
            tmp = 0
            for k in range(b[i] + 1 - a[i]):
                ary[k] += dp[i][j]
                ary[k] *= a[i] + k
                ary[k] %= mod
                tmp += ary[k]
                tmp %= mod
    return dp[n][c]


def __starting_point():
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(main1(n, c, a, b))


__starting_point()
