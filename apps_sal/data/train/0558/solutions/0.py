from queue import PriorityQueue
m,n=list(map(int,input().split()))
rr=[]
cc=[]
speed={'S':3,'O':2,'F':1}
visited=set()
dp=[]

def qwerty(cur,x,y,f):
	if f==0:
		gg=rr[x][1]+y*rr[x][0]
		while gg<cur:
			gg+=(2*(n-1))*rr[x][0]
		return gg-cur+rr[x][0]
	elif f==1:
		gg=rr[x][1]+(2*(n-1)-y)*rr[x][0]
		while gg<cur:
			gg+=(2*(n-1))*rr[x][0]
		return gg-cur+rr[x][0]
	elif f==2:
		gg=cc[y][1]+x*cc[y][0]
		while gg<cur:
			gg+=(2*(m-1))*cc[y][0]
		return gg-cur+cc[y][0]		
	elif f==3:
		gg=cc[y][1]+(2*(m-1)-x)*cc[y][0]
		while gg<cur:
			gg+=(2*(m-1))*cc[y][0]
		return gg-cur+cc[y][0]


dirx=[0, 0, 1, -1]
diry=[1, -1, 0, 0]

for i in range(m):
	o=[x for x in input().split()]
	o[0]=speed[o[0]]
	o[1]=int(o[1])
	rr.append(o)


for i in range(n):
	o=[x for x in input().split()]
	o[0]=speed[o[0]]
	o[1]=int(o[1])
	cc.append(o)


sx,sy,stt,dx,dy=list(map(int,input().split()))
sx-=1
sy-=1
dx-=1
dy-=1

for i in range(m):
	dp.append([10**9]*n)

dp[sx][sy]=stt
pq = PriorityQueue()
pq.put((stt, sx, sy))
while not pq.empty():
	#print(dp)
	(t,cxx,cyy)=pq.get()
	if (cxx,cyy) in visited:
		continue
	visited.add((cxx,cyy))
	for i in range(len(dirx)):
		nxx=cxx+dirx[i]
		nyy=cyy+diry[i]
		if nxx>=0 and nxx<m and nyy>=0 and nyy<n and (nxx,nyy) not in visited:
			coo=qwerty(dp[cxx][cyy],cxx,cyy,i)
			if coo+dp[cxx][cyy]<dp[nxx][nyy]:
					dp[nxx][nyy]=coo+dp[cxx][cyy]
					pq.put((dp[nxx][nyy],nxx,nyy))

print(dp[dx][dy])






	




