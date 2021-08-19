import sys
def input(): return sys.stdin.readline().rstrip("\r\n")


def inp(): return list(map(int, sys.stdin.readline().rstrip("\r\n").split()))


# ______________________________________________________________________________________________________
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
# segment tree for range minimum query
# sys.setrecursionlimit(10**5)
# n = int(input())
# a = list(map(int,input().split()))
# st = [float('inf') for i in range(4*len(a))]
# def build(a,ind,start,end):
#   if start == end:
#       st[ind] = a[start]
#   else:
#       mid = (start+end)//2
#       build(a,2*ind+1,start,mid)
#       build(a,2*ind+2,mid+1,end)
#       st[ind] = min(st[2*ind+1],st[2*ind+2])
# build(a,0,0,n-1)
# def query(ind,l,r,start,end):
#   if start>r or end<l:
#       return float('inf')
#   if l<=start<=end<=r:
#       return st[ind]
#   mid = (start+end)//2
#   return min(query(2*ind+1,l,r,start,mid),query(2*ind+2,l,r,mid+1,end))
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
# a = [0,1]
# for i in range(100000):
#     a.append(a[-1]+a[-2])
for _ in range(tc):
    n, = inp()
    print(1 if any([int(i) % 5 == 0 for i in str(n)]) else 0)
