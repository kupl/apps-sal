from scipy.sparse.csgraph import csgraph_from_dense,dijkstra

sx,sy,gx,gy=map(int,input().split())
n=int(input())
arr=[[sx,sy,0]]+[list(map(int,input().split())) for _ in range(n)]+[[gx,gy,0]]
g=[[-1]*(n+2) for _ in range(n+2)]
for i in range(n+2):
  x1,y1,r1=arr[i]
  for j in range(n+2):
    x2,y2,r2=arr[j]
    g[i][j]=max(0.0,((x1-x2)**2+(y1-y2)**2)**0.5-(r1+r2))
g=csgraph_from_dense(g,null_value=-1)
ans=((sx-gx)**2+(sy-gy)**2)**0.5
print(min(ans,dijkstra(g,indices=0)[n+1]))
