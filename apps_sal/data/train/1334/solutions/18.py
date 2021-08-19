import sys
# import math as mt
# from collections import Counter
# from itertools import permutations
# from functools import reduce
# from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace


def get_inpt(): return sys.stdin.readline().strip()
def get_int(): return int(sys.stdin.readline().strip())
def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_array(): return list(map(int, sys.stdin.readline().strip().split()))

# sys.setrecursionlimit(10**7)
# INF = float('inf')
# MOD1, MOD2 = 10**9+7, 998244353


n = get_int()
arr = get_array()

dp = [0 for _ in range(n)]

dp[-1] = arr[-1]
dp[-2] = arr[-2]
# dp[-3] = min(arr[-1], arr[-2], arr[-3])
dp[-3] = arr[-3]

for i in range(n - 4, -1, -1):

    dp[i] = arr[i] + min(dp[i + 1], dp[i + 2], dp[i + 3])

print(min(dp[0], dp[1], dp[2]))
