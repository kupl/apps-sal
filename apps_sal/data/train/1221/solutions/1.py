# cook your dish here
import math
t = int(input())
for _ in range(t):
 xf = int(input())
 ans = 0
 x,y = 0,0
 while x<=xf:
  p = int(math.sqrt(y))
  if p*p>y:
   x = p
   y = y + p*p
   ans = ans + 1
  else:
   x = p+1
   y = y + (p+1)*(p+1)
   ans = ans + 1
 if x<=xf:
  print(ans)
 else:
  print(ans-1)
