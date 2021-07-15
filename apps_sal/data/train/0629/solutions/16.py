# cook your dish here
for _ in range(int(input())):
 r,g,b,m=list(map(int,input().split()))
 r=list(map(int,input().split()))
 g=list(map(int,input().split()))
 b=list(map(int,input().split()))
 x=max(r)
 y=max(g)
 z=max(b)
 while m>0:
  if x>=y and x>=z:
   x//=2
  elif y>=x and y>=z:
   y//=2
  else:
   z//=2
  m-=1
 print(max(x,y,z))

