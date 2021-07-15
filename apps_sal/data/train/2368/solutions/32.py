import math
t=int(input())
for w in range(t):
    n=int(input())
    a=[int(i) for i in input().split()]
    b=[int(i) for i in input().split()]
    k1=min(a)
    k2=min(b)
    c=0
    for i in range(n):
        k3=a[i]-k1
        k4=b[i]-k2
        c+=max(k3,k4)
    print(c)
