import sys

def spaces(a,n,m,k,visit1,visit2,dist,position):
 queue = [position]
 lastedit = []
 dist[position[0]][position[1]] = 0 
 while queue!=[]:
  point = queue[0]
  i = point[0]
  j = point[1]
  #print 'point',i,j
  if visit1[i][j]==False:
   visit1[i][j] = True
   startx = max(i-k,0)
   endx = min(i+k,n-1)
   for x in range(startx,endx+1):
    starty = max(0,j+abs(x-i)-k)
    endy = min(m-1,j-abs(x-i)+k)
    for y in range(starty,endy+1):
     if (a[x][y]==0 and visit1[x][y]==False):
      if visit2[x][y]==True:
       lastedit.append([x,y])
      #print x,y,
      if dist[x][y]>dist[i][j]+1:
       dist[x][y]=dist[i][j]+1
       queue.append([x,y])
  #print queue,dist
  queue = queue[1:]
  #print
 return lastedit

for t in range(int(input())):
 n,m,k1,k2 = list(map(int,input().split()))
 a = []
 for i in range(n):
  a.append(list(map(int,input().split())))
 #print a
 value = sys.maxsize
 listing = []
 visit1 = [[False for i in range(m)]for j in range(n)]
 visit2 = [[False for i in range(m)]for j in range(n)]
 dist1 = [[sys.maxsize for i in range(m)]for j in range(n)]
 dist2 = [[sys.maxsize for i in range(m)]for j in range(n)]
 if k1>=k2:
  spaces(a,n,m,k1,visit1,visit2,dist1,[0,0])
 else:
  spaces(a,n,m,k2,visit1,visit2,dist1,[0,m-1])
  listing = spaces(a,n,m,k1,visit2,visit1,dist2,[0,0])
 if k1>k2:
  listing = spaces(a,n,m,k2,visit2,visit1,dist2,[0,m-1])
 #print visit1
 #sprint visit2
 if k1==k2:
  if dist1[0][m-1]==sys.maxsize:
   print('-1')
  else:
   print(int((dist1[0][m-1]+1)/2))
 else:
  d = len(listing)
  for i in range(d-1,-1,-1):
   x = listing[i][0]
   y = listing[i][1]
   if visit1[x][y]==True and dist2[x][y]<value:
    value = dist2[x][y]
  if value!=sys.maxsize:
   print(value)
  else:
   print('-1')




   
   

