# cook your dish here
import math
a,b=list(map(int,  input().split()))
l=[]
for x in range(1,a+1):
 for y in range(1,b+1):
  f=(x**2)+y
  r=math.sqrt(f)
  if int(r+0.5)**2==f:
   l.append(1)
  else:
   l.append(0)
print(sum(l))

