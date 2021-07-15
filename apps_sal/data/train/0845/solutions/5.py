import math as m
for _ in range(int(input())):
 a,b=map(int,input().split())
 g=m.gcd(a,b)
 print(a//g * b//g)
