def main():
    Q = int(input())
    data = []
    for _ in range(Q):
        N = int(input())
        S1 = [int(a) for a in list(input())]
        S2 = [int(a) for a in list(input())]
        data.append((N, [S1, S2]))
    A = [3, 4, 5, 6]
    B = [1, 2]
    for (N, S) in data:
        dp = [[0, 0] for _ in range(N + 1)]
        dp[0][0] = 1
        for n in range(N):
            if S[0][n] in A and S[1][n] in A:
                dp[n + 1][0] = dp[n][1]
                dp[n + 1][1] = dp[n][0]
            elif S[0][n] in B and S[1][n] in A:
                dp[n + 1][0] = dp[n][0]
                dp[n + 1][1] = 0
            elif S[0][n] in A and S[1][n] in B:
                dp[n + 1][0] = 0
                dp[n + 1][1] = dp[n][1]
            else:
                dp[n + 1][0] = dp[n][0]
                dp[n + 1][1] = dp[n][1]
        if dp[N][1] == 1:
            print('YES')
        else:
            print('NO')


def __starting_point():
    main()


__starting_point()
