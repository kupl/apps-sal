import sys
import math
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


def main():
    N, K = list(map(int, input().split()))
    mod = 998244353

    dp = [[0]*(N+1) for _ in range(N+1)]

    dp[0] = [1] + [0]*N

    for i in range(1, N+1):
        for j in range(i, 0, -1):
            dp[i][j] += dp[i-1][j-1]
            if j*2 <= N:
                dp[i][j] += dp[i][2*j]
            dp[i][j] %= mod

    print((dp[N][K]))


def __starting_point():
    main()

__starting_point()
