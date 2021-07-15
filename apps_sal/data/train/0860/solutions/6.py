# cook your dish here
import math
for _ in range(int(input())):
 n,hour=list(map(int,input().split()))
 l=list(map(int,input().split()))
 low,h=1,max(l)
 while low!=h:
  mid=(low+h)//2 
  count=0 
  for i in l:
   count+=math.ceil(i/mid)
  if count<=hour:
   h=mid 
  else:
   low=mid+1 
 print(low)
   

