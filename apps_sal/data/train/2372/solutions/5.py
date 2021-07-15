a=int(input())
from math import sqrt
for i in range(a):
    b=int(input())
    g=int(sqrt(b))
    if b!=1:
        ans=g-1
        if b%g==0:
            ans+=b//g-1
        else:
            ans+=b//g
        print(ans)
    else:print(0)

