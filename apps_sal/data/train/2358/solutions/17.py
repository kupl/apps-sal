from heapq import heappush,heappop
xs,ys,xt,yt = map(int,input().split())
n = int(input())
XY = [list(map(int,input().split())) for i in range(n)]
XY.append([xs,ys,0])
XY.append([xt,yt,0])
inf = 10**14
e = [[inf]*(n+2) for i in range(n+2)]
for i in range(n+1):
    for j in range(i+1,n+2):
        xi,yi,ri = XY[i]
        xj,yj,rj = XY[j]
        dif = max(0,((xi-xj)**2+(yi-yj)**2)**0.5-ri-rj)
        e[i][j] = e[j][i] = dif

h = []
heappush(h,(0,n))
dis = [inf]*(n+2)
dis[n] = 0
while h:
    cost,now = heappop(h)
    if cost > dis[now]:
        continue
    for nex,dif in enumerate(e[now]):
        if dis[nex] > dis[now]+dif:
            dis[nex] = dis[now]+dif
            heappush(h,(dis[nex],nex))
print(dis[-1])
