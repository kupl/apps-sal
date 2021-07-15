from math import *
for _ in range(int(input())):
 k,n = map(str, input().split())
 n = int(n)
 p = len(set(list(k)))
 if p == 1:
  print(1)
 else:
  p = p**3
  x = 1
  y = 1
  flag = 0
  for i in range(n):
   if x > p:
    flag = 1
    break
   x += (y*2)
   y *= 2
  if flag == 0:
   print(x-y)
  else:
   print(p)
