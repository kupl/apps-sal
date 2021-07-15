# cook your dish here
import heapq as hq
from math import floor
for _ in range(int(input())):
 n,a,b,x,y,z=list(map(int,input().split()))
 arr=[-int(i) for i in input().split()]
 days=floor((z-b)/y)
 if b+y*days==z:
  z+=1


 ans=0

 hq.heapify(arr)
 curr=a+days*x

 while curr<z :

  u=hq.heappop(arr)
  u=-u
  if u==0 :
   break
  else:
   curr+=u
   ans+=1
   hq.heappush(arr,-(u//2))

 if curr>=z:

  print(ans)
 else:
  print("RIP")






