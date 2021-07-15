import math
t=int(input())
for i in range(t):
    a,b=map(int,input().split(" "))
    c=math.gcd(a,b)
    l=(a*b)//c
    print(c," ",l)
