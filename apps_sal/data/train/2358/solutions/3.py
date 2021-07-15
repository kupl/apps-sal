import sys
input=sys.stdin.readline
sx,sy,tx,ty=list(map(int,input().split()))
n=int(input())
p=[(sx,sy,0)]
for _ in range(n):
  x,y,r=list(map(int,input().split()))
  p.append((x,y,r))
p.append((tx,ty,0))
n+=2
edge=[[]for _ in range(n)]
for i in range(n-1):
  for j in range(i+1,n):
    sx,sy,sr=p[i]
    tx,ty,tr=p[j]
    t=(abs(sx-tx)**2+abs(sy-ty)**2)**0.5
    c=max(0,t-(sr+tr))
    edge[i].append((j,c))
    edge[j].append((i,c))
from heapq import heappop,heappush
inf=10**20
ans=[inf]*n
ans[0]=0
root=[-1]*n
h=[(0,0)]
while h:
  c,v=heappop(h)
  if ans[v]<c:continue
  for u,t in edge[v]:
    if c+t<ans[u]:
      ans[u]=c+t
      root[u]=v
      heappush(h,(c+t,u))
print((ans[n-1]))

