import math
t=int(input())
for _ in range(t):
 a,b=map(int,input().split())
 l=list(map(int,input().split()))
 l1=sorted(l)
 k=0
 m=0
 for i in range(0,len(l1)):
  if l1[i]<=9 or l1[i]>=80:
   k=k+1
  else:
   m=m+1
 x1=math.ceil(k/b)
 x2=math.ceil(m/b)
 print(x1+x2)
