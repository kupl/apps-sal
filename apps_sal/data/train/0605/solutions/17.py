for _ in range(int(input())):
 n,m = map(int,input().split())
 s = input()
 r,l,u,d=0,0,0,0 #displacement from starting position
 x,y=0,0
 for i in s:
  if i=='U':
   y+=1
  elif i=='D':
   y-=1
  elif i=='R':
   x+=1
  else:
   x-=1
  if x>r:
   r=x
  elif x<l:
   l=x
  elif y>u:
   u=y
  elif y<d:
   d=y
 #print(u,d,l,r)
 if n>abs(u)+abs(d) and m>abs(l)+abs(r):
  print("safe")
 else:
  print("unsafe")
