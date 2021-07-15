import sys
# sys.setrecursionlimit(10**6) 
input=sys.stdin.readline
t=int(input())
import math
for t1 in range(t):
    # n=int(input())
    k,n=list(map(int,input().split(" ")))
    l=[]
    for i in range(k):
        s=input()
        s=s.strip()
        l.append(int(s,2))
    l.sort()
    a=0
    curr="0"+"1"*(n-1)
    curr=int(curr,2)
    temp=1<<n
    d={}
    for i in range(k):
        d[l[i]]=1
        if(temp%2==0):
            if(l[i]>curr):
                a=1
            else:
                
                while(d.get(curr+1,0)==1):
                    curr+=1
                curr+=1
                #increase by 1
        else:
            if(l[i]>=curr):
                while(d.get(curr-1,0)==1):
                    curr-=1
                #decrease by 1
                curr-=1
            else:
                a=1
        temp-=1
    z=bin(curr)[2:]
    if(len(z)<n):
        diff=n-len(z)
        z="0"*diff+z
    print(z)



