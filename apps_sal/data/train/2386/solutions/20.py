import math as mt 
import sys,string
input=sys.stdin.readline
L=lambda : list(map(int,input().split()))
Ls=lambda : list(input().split())
M=lambda : list(map(int,input().split()))
I=lambda :int(input())
from collections import defaultdict



t=I()
for _ in range(t):
    n=I()
    l=L()
    v=[0]*n
    a=[]
    for i in range(2*n):
        if(v[l[i]-1]==0):
            a.append(l[i])
            v[l[i]-1]=1
    print(*a)

