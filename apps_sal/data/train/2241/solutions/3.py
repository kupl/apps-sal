'''
研究室PCでの解答
'''
import math
import queue
import bisect
from collections import deque, defaultdict
import heapq as hpq
from sys import stdin, setrecursionlimit
ipt = stdin.readline
setrecursionlimit(10**7)
mod = 10**9 + 7


def main():
    n, c = list(map(int, ipt().split()))
    a = [int(i) for i in ipt().split()]
    b = [int(i) for i in ipt().split()]
    nj = [[] for j in range(c + 1)]
    nj[0] = [1] * 401
    for j in range(1, c + 1):
        for i in range(401):
            nj[j].append(nj[j - 1][i] * i % mod)
    snj = [[0] for j in range(c + 1)]
    for j in range(c + 1):
        sj = snj[j]
        ssj = nj[j]
        for i in range(1, 401):
            sj.append((sj[-1] + ssj[i]) % mod)
    dp = [snj[k][b[0]] - snj[k][a[0] - 1] for k in range(c + 1)]
    for i in range(1, n):
        ai = a[i]
        bi = b[i]
        for j in range(c, -1, -1):
            dp[j] = dp[j] * (bi - ai + 1) % mod
            for k in range(1, j + 1):
                dp[j] = (dp[j] + dp[j - k] * (snj[k][bi] - snj[k][ai - 1])) % mod

    print((dp[c] % mod))

    return None


def __starting_point():
    main()


__starting_point()
