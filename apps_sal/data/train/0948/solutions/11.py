# cook your dish here
a,b=map(int,input().strip().split(' '))
count=0
import math
r=int(math.sqrt(b))
for i in range(1,a+1):
  for j in range(1,b+1):
   r=i*i+j
   x=math.sqrt(r)
   if(int(x)==x):
    count+=1
print(count)
