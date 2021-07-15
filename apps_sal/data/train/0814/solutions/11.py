from collections import defaultdict
import math

for t in range(int(input())):
 n=int(input())
 store=list(map(int,input().split()))
 count=0
 curr=0
 cStore=defaultdict()
 maxi=0
 second=0
 
 for i in range(n):
  if store[i]==0:
   if curr>0:
    curr+=1
   else:
    curr=1
  else:
   if curr>maxi:
    second=maxi
    maxi=curr
   elif curr>second:
    second=curr
   curr=0
 if second!=0 and math.ceil(maxi/2)<second:
  print("No")
 else:
  if maxi%2==0:
   print("No")
  else:
   print("Yes")
  


   
 

