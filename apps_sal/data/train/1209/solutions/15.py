for t in range(int(input())):
 v1,t1,v2,t2,v3,t3=map(int,input().split())
 if t3>t2 or t3<t1:
  print("NO")
 else:
  if v1>= (v3*(t3-t2))/(t1-t2) and v2>=(v3*(t3-t1))/(t2-t1):
   print("YES")
  else:
   print("NO")
