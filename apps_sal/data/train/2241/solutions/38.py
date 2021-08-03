def main():
    mod = 10**9 + 7
    n, c = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    dp = [0] * (c + 1)
    dp[0] = 1
    ans = 0

    p = [[0] * (401) for _ in [0] * 401]  # p[i][j]でj^i
    for i in range(401):
        for j in range(401):
            p[i][j] = pow(j, i, mod)

    for a, b in zip(A, B):
        dp2 = [0] * (c + 1)
        q = [0] * (c + 1)
        for i in range(c + 1):
            q[i] = sum(p[i][a:b + 1]) % mod
        for i in range(c + 1):
            temp = 0
            for j in range(i + 1):
                temp += dp[i - j] * q[j]
            dp2[i] = temp % mod
        dp = dp2
    ans += dp[-1]
    print(ans % mod)


main()
