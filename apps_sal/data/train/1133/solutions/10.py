from fractions import gcd
from functools import reduce
t=int(input())
for _ in range(t):
 n = int(input())
 list1 = list(map(int, input().split()))
 r= reduce(gcd, list1)
 r1= sum(list1)//r
 print(r,r1)
