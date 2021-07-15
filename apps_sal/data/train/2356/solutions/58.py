import bisect, collections, copy, heapq, itertools, math, string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
from collections import deque, defaultdict, Counter
import heapq
from functools import reduce
from itertools import permutations
import math
import bisect

def main():
    mod = 998244353
    def comp(x, y):
        if x < y:
            return 0
        return dp[x][y]
    N, K = MI()
    dp = [[0 for _ in range(N + 1)]for _ in range(N + 1)]
    dp[0][0] = 1
    dp[0][1] = 0
    dp[1][0] = 0
    dp[1][1] = 1
    for i in range(2, N + 1):
        for j in range(N, 0, -1):
            dp[i][j] = comp(i - 1, j - 1) + comp(i, 2 * j)
            dp[i][j] %= mod
    #print(dp)
    print((dp[N][K]))
def __starting_point():
    main()

__starting_point()
