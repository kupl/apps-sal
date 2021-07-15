from collections import *
from bisect import *
from math import *
from heapq import *
import sys
input=sys.stdin.readline
t=int(input())
while(t):
    t-=1
    n,m,a,b=map(int,input().split())
    ma=[[0 for i in range(m)] for j in range(n)]
    x=-a
    flag=0
    for i in range(n):
        x=(x+a)%m
        for j in range(x,min(x+a,m)):
            ma[i][j]=1
        re=a-(m-x)
        for j in range(re):
            ma[i][j]=1
    for i in range(m):
        cc=0
        for j in range(n):
            if(ma[j][i]==1):
                cc+=1
        if(cc!=b):
            flag=1
            break
    if(flag):
        print("NO")
    else:
        print("YES")
        for i in ma:
            for j in i:
                print(j,end="")
            print()
    

