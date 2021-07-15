from math import sqrt

def solve():
 n = int(input())
 
 k = int(sqrt(n))
 
 y = n - k * k
 
 z = y % k
 
 if z > 0:
  print('X'*z+'D'+'X'*(k - z)+'D'*(k+y//k))
 else:
  print("X" * k + "D" * (k+y//k))
 
t = int(input())

for tt in range(0, t):
 solve()
