import math
def dist(w,x,y,z):
 return math.hypot(y - w, z - x)

t = int(input())
while (t>0):
 t = t -1
 n, m = list(map(int,input().split()))
 a = []
 for i in range(0,n):
  x,y = list(map(int,input().split()))
  a.append([x,y])
 for j in range(0,m):
  p,q,r,s = list(map(int,input().split()))
  nearest = -1
  distance = 10000000000
  for i in range(0,n):
   way = dist(a[i][0],a[i][1],p,q)
   if way < distance:
    distance = way
    nearest = i
  print(nearest + 1)
  a[nearest][0] = r
  a[nearest][1] = s


