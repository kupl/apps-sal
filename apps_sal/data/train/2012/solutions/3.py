'''
Created on

@author: linhz
'''
import sys
usedNum=0
n=int(input())
p=[0 for i in range(n+1)]
usedNum=0
if n%4==3 or n%4==2:
    print(-1)
else:
    i=1
    j=n
    a=1
    b=n
    while j>i:
        p[i]=a+1
        p[i+1]=b
        p[j]=b-1
        p[j-1]=a
        i+=2
        j-=2
        a+=2
        b-=2
    if j==i:
        p[i]=a
    ans=""
    for i in range(1,n+1):
        ans+=str(p[i])+" "
    print(ans)
