import sys
input = sys.stdin.readline
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations, accumulate
from heapq import heappush, heappop, heapify
from bisect import bisect_left, bisect_right

SI = lambda: input()
NI = lambda:int(input())
MI = lambda:map(int, input().split())
cutLF = lambda x:list(x)[:-1] if x[-1]=='\n' else list(x)
strLST = lambda:cutLF(input())

n,m=MI()
*a,=MI()
s=sum(a)
mod=10**9+7
hidari=[]
start=n+m
for i in range(n+s):
    hidari.append(start-i)
    
left=1
right=1
for i in range(n+s):
    left*=hidari[i]
    left%=mod
    right*=(i+1)
    right%=mod

print(left*pow(right,mod-2,mod)%mod)
