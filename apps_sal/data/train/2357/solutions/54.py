import sys
# import numpy as np
# from numba import njit, i8, void

MOD = 10**9 + 7

N, M = list(map(int, sys.stdin.readline().rstrip().split()))
# A = np.array([int(x) for x in sys.stdin.readline().rstrip().split()], dtype=np.int64)
A = [int(x) for x in sys.stdin.readline().rstrip().split()]


# @njit(void(i8, i8, i8[:]), cache=True)
def solve(N, M, A):

    S = sum(A)

    num = 1
    don = 1

    for i in range(1, S + N + 1):
        num = num * (M + N - (i - 1)) % MOD
        don = don * i % MOD

    ans = num * pow(don, MOD - 2, MOD) % MOD

    # print(INV)

    print(ans)


solve(N, M, A)
