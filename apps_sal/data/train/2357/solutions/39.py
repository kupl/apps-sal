import sys
MOD = 10 ** 9 + 7
(N, M) = list(map(int, sys.stdin.readline().rstrip().split()))
A = [int(x) for x in sys.stdin.readline().rstrip().split()]


def solve(N, M, A):
    S = sum(A)
    num = 1
    don = 1
    for i in range(1, S + N + 1):
        num = num * (M + N - (i - 1)) % MOD
        don = don * i % MOD
    ans = num * pow(don, MOD - 2, MOD) % MOD
    print(ans)


solve(N, M, A)
