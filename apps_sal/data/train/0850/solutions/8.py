import math
for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if  len(set(a))==1:
        print(2*a[0])
    else:
        a=list(set(a))
        x,p=0,0
        z=max(a)
        a.remove(z)
        for i in range(len(a)):
            x=math.gcd(x,a[i])

        y=max(a)
        a.append(z)
        a.remove(y)
        for i in range(len(a)):
            p=math.gcd(p,a[i])
        print(max(z+x,p+y))
