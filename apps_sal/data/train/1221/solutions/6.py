# cook your dish here
import math
for _ in range(int(input())):
 last=int(input())
 x=0
 y=0
 c=0
 while True:
  if y>=last*last:
   print(c)
   break
  c+=1
  x=int(math.sqrt(y))+1
  y=y+x*x




