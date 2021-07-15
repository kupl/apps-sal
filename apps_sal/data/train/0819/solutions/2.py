
import math
t=int(input())
for _ in range(t):
    a,b=(list(map(int,input().split())))
    if (math.gcd(a,b)==1):
        print("YES")
    else:
        print("NO")
    

