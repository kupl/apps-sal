# cook your dish here
test=int(input())
for _ in range(test):
 r,b,g,m=map(int,input().split())
 red=sorted(map(int,input().split()),reverse=True)
 blue=sorted(map(int,input().split()),reverse=True)
 green=sorted(map(int,input().split()),reverse=True)
 x,y,z=red[0],blue[0],green[0]
 for _ in range(m):
  k=max(x,y,z)
  if k==x:
   x=x//2
  elif k==y:
   y=y//2
  else:
   z=z//2
 print(max(x,y,z))
