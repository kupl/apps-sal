def main():
    A = input()
    N = len(A)
    a = ord('a')
    INF = N
    na = [[INF] * 26 for _ in range(N + 1)]
    for i in range(N - 1, -1, -1):
        c = ord(A[i]) - a
        for j in range(26):
            na[i][j] = na[i + 1][j]
        na[i][c] = i
    dp = [INF] * (N + 1)
    dp[N] = 1
    recon = [None] * (N + 1)
    for i in range(N - 1, -1, -1):
        for j in range(26):
            ni = na[i][j]
            if ni == N:
                if dp[i] > 1:
                    dp[i] = 1
                    recon[i] = (chr(a + j), N)
            elif dp[i] > dp[ni + 1] + 1:
                dp[i] = dp[ni + 1] + 1
                recon[i] = (chr(a + j), ni + 1)
    i = 0
    ans = []
    while i < N:
        (c, ni) = recon[i]
        ans.append(c)
        i = ni
    print(''.join(ans))


def __starting_point():
    main()


__starting_point()
