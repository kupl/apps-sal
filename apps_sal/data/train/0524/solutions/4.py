import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
inp = lambda: list(map(int,sys.stdin.readline().rstrip("\r\n").split()))
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
# import sys
sys.setrecursionlimit(10**5)
# n = int(sys.stdin.readline().strip())
# a = list(map(int,sys.stdin.readline().strip().split()))
a = str(input())
n = len(a)
st = [float('inf') for i in range(4*len(a))]
def build(a,ind,start,end):
	if start == end:
		st[ind] = [a[start]] if ord(a[start])%2==0 else []
	else:
		mid = (start+end)//2
		build(a,2*ind+1,start,mid)
		build(a,2*ind+2,mid+1,end)
		st[ind] = list(set(st[2*ind+1]+st[2*ind+2]))
build(a,0,0,n-1)
def query(ind,l,r,start,end):
	if start>r or end<l:
		return []
	if l<=start<=end<=r:
		return st[ind]
	mid = (start+end)//2
	return list(set(query(2*ind+1,l,r,start,mid)+query(2*ind+2,l,r,mid+1,end)))
for i in range(int(input())):
	l,r = inp()
	ans = query(0,l-1,r-1,0,n-1)
	# print(ans)
	print(len(ans))
# tc = 1
# # tc, = inp()
# for _ in range(tc):
#     # s = str(input())
#     a = [i for i in input().split()]
#     k = min(a,key = lambda x:len(x))
#     print(k)

