#分岐は後で処理すれば良い
#それぞれ0,nに近づくのが最適
from heapq import heappush,heappop
inf=10**10
n=int(input())
l=[[] for i in range(n+1)]
for i in range(n-1):
  a,b=map(int,input().split())
  l[a].append(b)
  l[b].append(a)
def dijkstra(s):
  q=[(0,s)]
  dist=[inf]*(n+1)
  dist[s]=0
  while q:
    c,v=heappop(q)
    if dist[v]<c:
      continue
    for i in l[v]:
      t=i
      cost=1
      if dist[v]+cost<dist[t]:
        dist[t]=dist[v]+cost
        heappush(q,[dist[t],t])
  return dist
d1=dijkstra(1)
d2=dijkstra(n)
countp=0
counts=0
for i in range(1,n+1):
  if d1[i]>d2[i]:
    counts+=1
  else:
    countp+=1
if countp>counts:
  print("Fennec")
else:
  print("Snuke")
