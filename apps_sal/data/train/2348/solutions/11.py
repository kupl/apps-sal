def examE():
    N = I()
    X = LI()
    L = I(); Q = I()
    n = N.bit_length()+1
    dp = [[0] * n for _ in range(N)]
    for i in range(N):
        dp[i][0] = bisect.bisect_right(X, X[i] + L) - 1
    for i in range(1, n):
        for j in range(N):
            if dp[j][i - 1] < N:
                index = dp[dp[j][i - 1]][i - 1]
                if index == j:
                    dp[j][i] = N
                else:
                    dp[j][i] = index
            else:
                dp[j][i] = N
    def fast_day(a, b):
        if a > b:
            a, b = b, a
        res = 0
        for i in range(n):
            if a >= b:
                return res
            c = max(0, bisect.bisect_left(dp[a], b) - 1)
            #最低かかる2**?の日数
            a = dp[a][c]
            #そこまで行く
            res += 2 ** c
    for _ in range(Q):
        a, b = list(map(int, input().split()))
        print((fast_day(a - 1, b - 1)))
#    print(dp)

import sys,copy,bisect,itertools,heapq,math
from heapq import heappop,heappush,heapify
from collections import Counter,defaultdict,deque
def I(): return int(sys.stdin.readline())
def LI(): return list(map(int,sys.stdin.readline().split()))
def LS(): return sys.stdin.readline().split()
def S(): return sys.stdin.readline().strip()
mod = 10**9 + 7
inf = float('inf')

examE()

