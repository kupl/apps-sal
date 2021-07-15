# cook your dish here
import math
a,b=map(int,input().split())
x=1
y=1
res=0
for i in range(1,a+1):
 for j in range(1,b+1):
  temp=i*i+j
  sr=math.sqrt(temp)
  if sr-math.floor(sr)==0:
   res+=1
print(res)
