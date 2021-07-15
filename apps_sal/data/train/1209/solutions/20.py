tc = int(input())
while(tc!=0):
 tc-=1
 v1,t1,v2,t2,v3,t3 = map(int,input().split())
 if t1==t3 and t3==t2:
  if v1+v2>=v3:
   print("YES")
  else:
   print("NO")
  continue
 elif t1==t2:
  if v1>=v3:
   print("YES")
  else:
   print("NO")
  continue
 l = v3*(t1-t3)/(t1-t2)
 r = (v1+v2)*(t1-t3)/(t1-t2)
 l1 = v3*(t3-t2)/(t1-t2)
 r1 = (v1+v2)*(t3-t2)/(t1-t2)
 # print(l,r)
 # print(l1,r1)
 if l<=min(v2,r) and l1<=min(v1,r1):
  print("YES")
 else:
  print("NO")
