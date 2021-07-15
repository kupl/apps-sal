from math import gcd
t=int(input())
for _ in range (t):
    n,m=map(int,input().split())
    if (n%m==0 or m%n==0):
        print(max(m,n))
    else:
        g=max(n,m)
        great=g
        while (True):
            if (great%n==0 and great%m==0):
                break
            else:
                great+=g
        print(great)
