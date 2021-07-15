t=int(input())
for i in range(t):
 ans=0
 x,y=list(map(int,input().split()))
 if y>x:
  if (y-x)%4==0:ans=3
  elif (y-x)%2==0: ans=2
  else: ans=1
 if y<x:
  if (y-x)%2==0:ans=1
  else: ans=2
 print(ans)

