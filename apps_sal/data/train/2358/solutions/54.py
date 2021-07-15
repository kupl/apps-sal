inf=10**18
def D(a,b,c,d):
	return ((c-a)**2+(d-b)**2)**0.5
xs,ys,xt,yt=map(int,input().split())
n=int(input())
xyr=[(xs,ys,0)]
for i in range(n):
	xyr.append(tuple(map(int,input().split())))
xyr.append((xt,yt,0))
dis=[[inf]*(n+2) for i in range(n+2)]
for i in range(n+2):
	dis[i][i]=0
for i in range(n+2):
	for j in range(i):
		a,b,r1=xyr[i]
		c,d,r2=xyr[j]
		r=D(a,b,c,d)-(r1+r2)
		r=max(0,r)
		dis[i][j]=r
		dis[j][i]=r
cost=[inf]*(n+2)
cost[0]=0
visited=[0]*(n+2)
now=0
for i in range(n+2):
	visited[now]=1
	MIN=inf
	pre_now=-1
	for j in range(n+2):
		if visited[j]==0:
			cost[j]=min(cost[now]+dis[now][j],cost[j])
			if MIN>cost[j]:
				MIN=cost[j]
				pre_now=j
	now=pre_now			
print(cost[n+1])
