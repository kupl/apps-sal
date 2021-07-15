from sys import stdin
input = lambda: stdin.readline().rstrip("\r\n")
inp = lambda: list(map(int,stdin.readline().rstrip("\r\n").split()))
#______________________________________________________________________________________________________
# from math import *
# from bisect import *
# from heapq import *
# from collections import defaultdict as dd
# from collections import OrderedDict as odict
# from collections import Counter as cc
# from collections import deque
# sys.setrecursionlimit(2*(10**5)+100) this is must for dfs
# mod = 10**9+7; md = 998244353
# ______________________________________________________________________________________________________
# Checking prime in O(root(N))
# def isprime(n):
#     if (n % 2 == 0 and n > 2) or n == 1: return 0
#     else:
#         s = int(n**(0.5)) + 1
#         for i in range(3, s, 2):
#             if n % i == 0:
#                 return 0
#         return 1
# def lcm(a,b):
#   return (a*b)//gcd(a,b)
# ______________________________________________________________________________________________________
# nCr under mod
# def C(n,r,mod):
#   if r>n:
#       return 0
#   num = den = 1
#   for i in range(r):
#       num = (num*(n-i))%mod
#       den = (den*(i+1))%mod
#   return (num*pow(den,mod-2,mod))%mod
# M = 10**5 +10
# ______________________________________________________________________________________________________
# For smallest prime factor of a number
# M = 1000010
# pfc = [i for i in range(M)]
# def pfcs(M):
#   for i in range(2,M):
#       if pfc[i]==i:
#           for j in range(i+i,M,i):
#               if pfc[j]==j:
#                   pfc[j] = i
#   return
# pfcs(M)
# ______________________________________________________________________________________________________
tc = 1
tc, = inp()
for _ in range(tc):
    s = str(input())
    d = [98, 57, 31, 45, 46]
    a = [ord(i)-ord('A') for i in s]
    d = [(a[i]+d[i])%26 for i in range(len(s))]
    ans = [chr(i+ord('A')) for i in d]
    print(''.join(ans))
