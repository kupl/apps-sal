import math as mt 
import sys,string
input=sys.stdin.readline
import random
from collections import deque,defaultdict
L=lambda : list(map(int,input().split()))
Ls=lambda : list(input().split())
M=lambda : list(map(int,input().split()))
I=lambda :int(input())
def bfs(a):
    w=g[a]
    v=[0]*n
    for i in w:
        v[i]=1
    v[a]=1
    j=0
    while(j<len(w)):
        k=w[j]
        for i in g[k]:
            if(v[i]==0):
                if(l[i]==l[k]):
                    w.append(i)
                    v[i]=1
                else:
                    return False
        j+=1
    return True
n=I()
g=[]
for i in range(n):
    g.append([])
x=[]
for _ in range(n-1):
    a,b=M()
    a-=1
    b-=1
    x.append((a,b))
    g[a].append(b)
    g[b].append(a)
l=L()
for i in range(n-1):
    if(l[x[i][0]]!=l[x[i][1]]):
        if(bfs(x[i][0])):
            print("YES")
            print(x[i][0]+1)
            return
        if(bfs(x[i][1])):
            print("YES")
            print(x[i][1]+1)
            return
        else:
            print("NO")
            return
print("YES")
print("1")

