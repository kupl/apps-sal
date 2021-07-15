import math
from sys import stdin
input=stdin.readline
for _ in range(int(input())):
 v1,t1,v2,t2,v3,t3=list(map(int,input().split()))
 if (v1>=v3 and t1==t2) or (v2>=v3 and t2==t3):
  print("YES")
  continue
 else:
  vx=(v3*(t3-t2))//(t1-t2)
  vy=v3*((t1-t3)/(t1-t2))
  if (0<=vx<=v1 and 0<=vy<=v2): 
   print("YES")
  else:
   print("NO")
  

