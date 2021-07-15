import io, sys, os
import math as ma
from decimal import Decimal as dec
from itertools import permutations
from itertools import combinations


def li():
 return list(map(int, sys.stdin.readline().split()))


def num():
 return list(map(int, sys.stdin.readline().split()))


def nu():
 return int(input())


def find_gcd(x, y):
 while (y):
  x, y = y, x % y
 return x


def lcm(x, y):
 gg = find_gcd(x, y)
 return (x * y // gg)


mm = 1000000007


def solve():
 t = nu()
 for tt in range(t):
  n=nu()
  s=input()
  x=""
  y=""
  for i in range(len(s)):
   if(i%2==0):
    x+="0"
    y+="1"
   else:
    x+="1"
    y+="0"
  cc=0
  pp=0
  for i in range(len(s)):
   if(s[i]!=x[i]):
    cc+=1
   if(s[i]!=y[i]):
    pp+=1
  print(min(cc,pp))



def __starting_point():
 solve()

__starting_point()
