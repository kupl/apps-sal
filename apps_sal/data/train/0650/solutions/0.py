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
def input(): return sys.stdin.readline().strip()


def inp(): return list(map(int, sys.stdin.readline().strip().split()))


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
# ______________________________________________________
for _ in range(int(input())):
    n, k = map(int, input().split())
    d = [[] for i in range(k + 1)]
    for i in range(n):
        l, r, p = map(int, input().split())
        d[p].append([l, r])
    ans = 0
    for i in d:
        if len(i) == 0:
            continue
        ans += 1
        t = sorted(i, key=lambda x: (x[1], x[0]))
        final = t[0][1]
        for j in range(1, len(t)):
            if t[j][0] >= final:
                ans += 1
                final = t[j][1]
    print(ans)
