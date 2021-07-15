n,m=map(int,input().split())
a=[]
for i in range(n):a.append(list(map(int,input().split())))
dpa=[[[0,0] for i in range(m+2)] for i in range(n+2)]
dpb=[[[0,0] for i in range(m+2)] for i in range(n+2)]
ans=0
for i in range(1,n+1):
	for j in range(1,m+1):
		dpa[i][j][0]=max(dpa[i-1][j][0],dpa[i][j-1][0])+a[i-1][j-1]
		dpa[n+1-i][m+1-j][1]=max(dpa[n+2-i][m+1-j][1],dpa[n+1-i][m+2-j][1])+a[n-i][m-j]
for i in range(n,0,-1):
	for j in range(1,m+1):
		dpb[i][j][0]=max(dpb[i+1][j][0],dpb[i][j-1][0])+a[i-1][j-1]
		dpb[n+1-i][m+1-j][1]=max(dpb[n-i][m+1-j][1],dpb[n+1-i][m+2-j][1])+a[n-i][m-j]
for i in range(2,n):
	for j in range(2,m):
		x=dpa[i-1][j][0]+dpa[i+1][j][1]+dpb[i][j-1][0]+dpb[i][j+1][1]
		y=dpb[i+1][j][0]+dpb[i-1][j][1]+dpa[i][j-1][0]+dpa[i][j+1][1]
		ans=max(ans,x,y)
print(ans)
