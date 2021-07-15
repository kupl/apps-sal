from math import *
t=int(input())
for i in range(t):
 a,b=map(int,input().split())
 a=int(a)
 b=int(b)
 print(2*gcd(a,b))
