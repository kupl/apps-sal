from functools import reduce
from fractions import gcd
import math
import bisect
import itertools
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
INF = float('inf')


def main():
    N = int(input())
    x = list(map(int, input().split()))
    L = int(input())
    Q = int(input())
    LOG = 30
    nxt = [[-1] * N for _ in range(LOG)]
    for i in range(N):
        nxt[0][i] = bisect.bisect_left(x, x[i] + L + 1) - 1
    for k in range(LOG - 1):
        for i in range(N):
            if nxt[k][i] == -1:
                nxt[k + 1][i] = -1
            else:
                nxt[k + 1][i] = nxt[k][nxt[k][i]]
    for _ in range(Q):
        (a, b) = map(int, input().split())
        if a > b:
            (a, b) = (b, a)
        a -= 1
        b -= 1
        ans = 0
        for k in reversed(range(LOG)):
            if nxt[k][a] < b:
                a = nxt[k][a]
                ans += 2 ** k
        print(ans + 1)


def __starting_point():
    main()


__starting_point()
