# cook your dish here
from math import gcd
def lcm(a,b):
 return (a*b)//gcd(a,b)
for a0 in range(int(input())):
 n=int(input())
 haha=list(map(int, input().split()))
 x=haha[0]
 for i in range(1,3):
  x=lcm(x,haha[i])
 x/=24
 print(int(n//x))

