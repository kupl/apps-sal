ma = lambda :map(int,input().split())
lma = lambda :list(map(int,input().split()))
tma = lambda :tuple(map(int,input().split()))
ni = lambda:int(input())
yn = lambda fl:print("Yes") if fl else print("No")
ips = lambda:input().split()
import collections
import math
import itertools
import heapq as hq
import sys
n,t = ma()
A = lma()
INF=10**15

mns = [INF]*(n+1) ##mxs[i] :: max(A[i:n])
for i in range(n):
    mns[i] = min(mns[i-1],A[i])
c = 0
dmx = -1
for i in range(1,n):
    if A[i]-mns[i] >dmx:
        dmx=A[i]-mns[i]
        c=1
    elif A[i]-mns[i] ==dmx:
        c+=1
print(c)

