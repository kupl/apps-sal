from heapq import heappush,heappop,heapify
INF=10**30

def dijkstra(G,s,n):
    que=[(0,s)]
    dist=[INF]*n
    dist[s]=0
    while que:
        mincost,u=heappop(que)
        if(mincost>dist[u]):
            continue
        for c,v in G[u]:
            if(dist[u]+c<dist[v]):
                dist[v]=dist[u]+c
                heappush(que,(dist[v],v))
    return dist

sx,sy,gx,gy=map(int,input().split())
N=int(input())
X,Y,R=[sx,gx],[sy,gy],[0,0]
for i in range(N):
    t,m,p=map(int,input().split())
    X.append(t);Y.append(m);R.append(p)
G=[[] for i in range(N+2)]
for i in range(N+2):
    for j in range(i):
        d=max(0,((X[i]-X[j])**2+(Y[i]-Y[j])**2)**0.5-R[i]-R[j])
        G[i].append((d,j))
        G[j].append((d,i))
dist=dijkstra(G,0,N+2)
print(dist[1])
