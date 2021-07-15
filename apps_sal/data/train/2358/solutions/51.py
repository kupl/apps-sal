from heapq import heappop,heappush
from math import sqrt
def distf(xyr,i,j):
  x,y,r=xyr[i]
  x1,y1,r1=xyr[j]
  d=max(0,sqrt((x-x1)**2+(y-y1)**2)-r-r1)
  return d

def main():
  xs,ys,xt,yt=list(map(int,input().split()))
  n=int(input())
  xyr=[list(map(int,input().split())) for _ in range(n)]
  xyr.append([xs,ys,0])
  xyr.append([xt,yt,0])
  inf=float('inf')
  dist=[[inf]*(n+2) for _ in range(n+2)]
  for i in range(n+2):
    dist[i][i]=0
  for i in range(n+1):
    for j in range(i+1,n+2):
      dist[i][j]=distf(xyr,i,j)
      dist[j][i]=dist[i][j]
  seen=[inf]*(n+2)
  seen[n]=0
  mi=set(range(n+2))
  while mi:
    d,v=inf,-1
    for j in mi:
      if d>seen[j]:
        d=seen[j]
        v=j
    mi.remove(v)
    for nv in mi:
      nd=dist[v][nv]
      if seen[nv]>seen[v]+nd:
        seen[nv]=seen[v]+nd
  print((seen[n+1]))
def __starting_point():
  main()

__starting_point()
