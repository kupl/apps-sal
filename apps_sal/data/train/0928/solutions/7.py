import sys
# import math
from math import gcd
# import re
# from heapq import *
# from collections import defaultdict as dd
# from collections import OrderedDict as odict
# from collections import Counter as cc
# from collections import deque
# sys.setrecursionlimit(10**5)#thsis is must
# mod = 10**9+7; md = 998244353
# m = 2**32
input = lambda: sys.stdin.readline().strip()
inp = lambda: list(map(int,sys.stdin.readline().strip().split()))
# def C(n,r,mod):
#   if r>n:
#       return 0
#   num = den = 1
#   for i in range(r):
#       num = (num*(n-i))%mod
#       den = (den*(i+1))%mod
#   return (num*pow(den,mod-2,mod))%mod
# M = 1000000+1
# pfc = [i for i in range(M+1)]
# def pfcs(M):
#     for i in range(2,M+1):
#         if pfc[i]==i:
#             for j in range(i+i,M+1,i):
#                 if pfc[j]==j:
#                     pfc[j] = i
#     return
#______________________________________________________
for _ in range(int(input())):
    n = int(input())
    ans = 0 
    for i in range(1,n+1):
        d = i*i
        if d>n:
            break
        if d%3!=0:
            ans+=1
    print(ans)
