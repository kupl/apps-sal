import sys
import math
from collections import defaultdict


def input():
    return sys.stdin.readline().rstrip()


def main():
    N, K = list(map(int, input().split()))
    mod = 998244353

    dp = [0] * (N + 1)

    dp[0] = 1

    for i in range(1, N + 1):
        for j in range(i, -1, -1):
            dp[j] = dp[j - 1]
            if j * 2 <= N:
                dp[j] += dp[2 * j]
            dp[j] %= mod

    print((dp[K]))


def __starting_point():
    main()


__starting_point()
