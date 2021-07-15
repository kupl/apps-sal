# cook your dish here
from collections import defaultdict
import math
t=int(input())
for it in range(t):
    k=input()
    n=int(input())
    d=defaultdict(list)
    for i in range(n):
        p=list(map(int,input().split()))
        d[p[0]].append(p[1])
    for r in d.keys():
        d[r]=sorted(d[r])
        d[r]=reversed(d[r])
    xa=-1
    xb=-1
    m=0
    g=[]
    for r in d.keys():
        g.append(r)
    g.sort()
    for r in g:
        s=d[r]
        x=r 
        for j in s:
            y=j
            if(xa==-1 and xb==-1):
                xa=x
                xb=y
            q=x-xa
            q=q*q
            p=y-xb
            p=p**2
            q=q+p
            q=math.sqrt(q)
            m=m+q
            xa=abs(x)
            xb=abs(y)
    m=round(m,2)
    print("%.2f"%m)
            
