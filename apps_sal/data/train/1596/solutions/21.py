# cook your dish here
from math import log
for _ in range(int(input())):
 x,y = map(int,input().split())
 x += 1
 y += 1
 c1,c2 = 0,0
 while x>0:
  x = x - 2**int(log(x,2))
  c1 += 1
 while y>0:
  y = y - 2**int(log(y,2))
  c2 += 1
 if c1==c2:
  print(0,0)
 elif c1>c2:
  print(2,c1-c2)
 else:
  print(1,c2-c1)
