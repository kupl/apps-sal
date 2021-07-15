# cook your dish here
import math
t=int(input())
while(t>0):
    t-=1 
    n=int(input())
    a=list(map(int,input().split()))
    m=min(a)
    ans=n/m
    print(math.ceil(ans))
