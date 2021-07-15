import re
import math as mt
def __starting_point():
 T=int(input())
 while T:
  n=int(input())
  lt=[int(x) for x in input().split()]
  p=0
  sm=sum(lt)
  for x in range(n):
   p=mt.gcd(p,lt[x])
   
 
  print(p,sm//p)
  T=T-1
__starting_point()
