import math
_1_50 = 1 << 50
def isqrt(x):
 if x < 0:
  raise ValueError('square root not defined for negative numbers')
 if x < _1_50:
  return int(math.sqrt(x)) 
 n = int(x)
 if n <= 1:
  return n 

 r = 1 << ((n.bit_length() + 1) >> 1)
 while True:
  newr = (r + n // r) >> 1 
  if newr >= r:
   return r
  r = newr

for i in range(int(input())):
 n=int(input())
 x=(isqrt(4*2*n+1)-1)//2
 
 x=x*(x+1)//2
 print(n-x)

