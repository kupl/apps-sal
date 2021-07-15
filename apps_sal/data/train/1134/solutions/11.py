__author__ = 'Deepak'
import math
t=int(input())
while(t>0):
 t-=1
 n,m=list(map(int,input().split()))
 a=list(map(int, input().split()))
 army=sum(a[:m])
 for i in range(m,len(a)):
  army=army-int(a[i]/2)+1
  if(army<=0):
   print("DEFEAT")
   break
 if(army>0):
  print("VICTORY")
