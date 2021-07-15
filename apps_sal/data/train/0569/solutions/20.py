import math
for _ in range(int(input())):
 n = int(input())
 d = math.floor(math.sqrt(1+(8*n)))
 d = ((d-1)//2)
 s = ((d*(d+1))//2)
 if s==n:
  print(0)
 else:
  print(n-s)
