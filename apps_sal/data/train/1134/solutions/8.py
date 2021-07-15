# cook your code here
from math import ceil
for _ in range(int(input())):
 n,m=list(map(int,input().split()))
 army=list(map(int,input().split()))
 sum=0
 for i in range(m):
  sum+=army[i]
 f=0
 for i in range(m,n):
  sum-=ceil(army[i]/2)
  if(sum<0):
   f=1
   break
 if f==0:
  print("VICTORY")
 else:
  print("DEFEAT")
