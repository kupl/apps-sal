# cook your dish here
import math
t = int(input())
while(t):
 n = int(input())
 res = 0
 x = 0
 y = 0
 while(x <= n):
  tmp = int(math.sqrt(y))
  tmp += 1
  y += tmp * tmp
  x = tmp
  res += 1
 
 print(res - 1)
 
 t -= 1
