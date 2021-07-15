from math import gcd
for _ in range(int(input())):
    x,y=list(map(int,input().split()))
    if gcd(x,y)>1:
        print("NO")
    else:
        print("YES")

