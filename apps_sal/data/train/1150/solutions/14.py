import math
for t in range(int(input())):
 n=int(input())
 c=0
 while n>0:
  r=int(math.sqrt(n))
  n=n-(r*r)
  c+=1 
 print(c)
 

