# cook your dish here
import math
for t in range(int(input())):
 n=int(input())
 l=list(map(int,input().split()))
 ans=l[0]
 z=0
 for i in range(1,len(l)):
  ans=math.gcd(l[i],ans)
  if ans==1:
   z=i+1
  else:
   continue
 if(z>1):
  print(z)
 else:
  print(-1)



