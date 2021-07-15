import math
n=int(input())
l=[]
for i in range(0,n):
 n1=int(input())
 count=0
 while n1>0:
  s=int(math.sqrt(n1))
  n1=n1-(s*s)
  count+=1 
 l.append(count)
for i in l:
 print(i)


