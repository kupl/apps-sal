import sys


def main(N, C, A, B):
    import sys
    input = sys.stdin.readline
    mod = 10**9 + 7
    powA = [[0] * (401) for i in range(401)]
    for i in range(401):
        for j in range(401):
            powA[i][j] = pow(i, j, mod)

    S = [[0] * 401 for i in range(C + 1)]
    for i in range(C + 1):
        S[i][0] = 0
    for i in range(C + 1):
        for j in range(1, 401):
            S[i][j] = (S[i][j - 1] + powA[j][i]) % mod

    dp = [[0] * (C + 1) for i in range(N)]
    for i in range(C + 1):
        dp[0][i] = S[i][B[0]] - S[i][A[0] - 1]
    for i in range(1, N):
        for j in range(C + 1):
            tmp = 0
            for k in range(j + 1):
                tmp = (tmp + (S[k][B[i]] - S[k][A[i] - 1]) * dp[i - 1][j - k]) % mod
            dp[i][j] = tmp
    print(dp[N - 1][C])


def main2(N, C, A, B):
    import sys
    input = sys.stdin.readline
    mod = 10**9 + 7
    powA = [[0] * (401) for i in range(401)]
    for i in range(401):
        for j in range(401):
            powA[i][j] = pow(i, j, mod)

    S = [[0] * 400 for i in range(C + 1)]
    for i in range(C + 1):
        S[i][0] = 1
    for i in range(C + 1):
        for j in range(1, 400):
            S[i][j] = (S[i][j - 1] + powA[j + 1][i]) % mod

    dp = [[0] * (C + 1) for i in range(N)]
    for i in range(C + 1):
        dp[0][i] = pow(A[0], i, mod)
    for i in range(1, N):
        for j in range(C + 1):
            tmp = 0
            for k in range(j + 1):
                tmp = (tmp + powA[A[i]][k] * dp[i - 1][j - k]) % mod
            dp[i][j] = tmp
    print(dp[N - 1][C])


input = sys.stdin.readline
N, C = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

if A == B:
    main2(N, C, A, B)
else:
    main(N, C, A, B)
