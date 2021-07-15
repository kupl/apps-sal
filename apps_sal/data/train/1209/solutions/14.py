t = int(input())

for i in range(t):
 v1,t1,v2,t2,v3,t3 = map(int,input().strip().split())
 
 vx = t2 - t3
 vy = t3 - t1
 
 if(t1<=t3<=t2):
  if((vx * v3 <= (vx + vy) * v1)and(vy * v3 <= (vx + vy) * v2)):
   print("YES")
  else:
   print("NO") 
 else:
   print("NO") 
