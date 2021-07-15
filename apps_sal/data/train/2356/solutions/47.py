import sys
try:
    import os
    f = open('input.txt', 'r')
    sys.stdin = f
except FileNotFoundError:
    None
from math import sqrt, ceil, floor
from collections import deque, Counter, defaultdict
# defaultdict(int)
input=lambda: sys.stdin.readline().strip()
sys.setrecursionlimit(11451419)
from decimal import ROUND_HALF_UP,Decimal  #変換後の末尾桁を0や0.01で指定
  #Decimal((str(0.5)).quantize(Decimal('0'), rounding=ROUND_HALF_UP))
from functools import lru_cache
from bisect import bisect_left as bileft, bisect_right as biright, insort
from itertools import combinations as com, permutations as per
from fractions import Fraction as frac  #frac(a,b)で正確なa/b
# @lru_cache(maxsize=10**10)
#######ここまでテンプレ#######
#ソート、"a"+"b"、再帰ならPython3の方がいい
#######ここから天ぷら########

n,k=list(map(int,input().split()))
mod=998244353
# @lru_cache(maxsize=10**10)
# def saiki(n,k):
#     print(n,k,flush=1)
#     if n<k:return 0
#     if n==k:return 1
#     if n==0:return 0
#     if k==0: return 0
#     if n==1:return 1
#     if k==1: return saiki(n,2*k)
#     return (saiki(n-1,k-1)+ saiki(n,2*k))%mod

dp=[[0]*3002 for  i in range(3003)]
# dp[1][1]=1
for i in range(1,n+1):
    for j in range(n,0,-1):
        if i<j:dp[i][j]=0
        elif i==j : dp[i][j]=1
        elif 2*j >i: dp[i][j]=dp[i-1][j-1]
        else: dp[i][j]=(dp[i-1][j-1]+ dp[i][2*j])%mod

print((dp[n][k]))

