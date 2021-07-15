from fractions import gcd
from functools import reduce

t=int(input())
for i in range(0,t):
 n=int(input())
 a=list(map(int,input().split()))
 r1= reduce(gcd, a)
 r2= sum(a)//r1
 print(r1,r2)

