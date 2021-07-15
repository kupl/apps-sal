# cook your dish here
import math
for _ in range(int(input())):
    n=int(input())
    a=map(int,input().split())
    a=list(a)
    x=a[0]
    for i in a:
        x=math.gcd(i,x)
    if x==1:
        k=-1
    else:
        k=x
        x1=x**0.5
        t=int(x1)
        for i in range(2,t+1):
            if(x%i==0):
                k=i
                break
    print(k)
