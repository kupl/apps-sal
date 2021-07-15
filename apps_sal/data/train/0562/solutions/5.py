n,m=list(map(int,input().split()))
grid=[ list(map(int,list(input()))) for i in range(n)]
obs0=[ [ 0 for j in range(m)] for i in range(n)] 
obs1=[ [ 0 for j in range(m)] for i in range(n) ]
max_side=min(m,n)
side_c=[ 40000 for i in range(max_side+1)]
side_c[0]=0
side_c[1]=0
#print(grid)
for i in range(n):
	for j in range(m):
		if (i+j)%2==0:
			obs0[i][j]=0
			obs1[i][j]=1
		else:
			obs0[i][j]=1
			obs1[i][j]=0
#print(obs0)
#print(obs1)
for i in range(n):
	for j in range(m):
		if obs0[i][j]!=grid[i][j]:
			obs0[i][j]=1
		else:
			obs0[i][j]=0
		if obs1[i][j]!=grid[i][j]:
			obs1[i][j]=1
		else:
			obs1[i][j]=0
#print(obs0)
#print(obs1)

for i in range(n):
	for j in range(1,m):
		obs0[i][j]+=obs0[i][j-1]
		obs1[i][j]+=obs1[i][j-1]
for j in range(m):
	for i in  range(1,n):
		obs0[i][j]+=obs0[i-1][j]
		obs1[i][j]+=obs1[i-1][j]
for side in range(2,max_side+1):
	for i in range(n):
		for j in range(m):
			if i+side>n or j+side>m:
				continue
			count0 = obs0[i+side-1][j+side-1] + (i!=0 and j!=0)*obs0[i-1][j-1] -(j!=0)*obs0[i+side-1][j-1] -(i!=0)*obs0[i-1][j+side-1] 
			count1 = obs1[i+side-1][j+side-1] + (i!=0 and j!=0)*obs1[i-1][j-1] -(j!=0)*obs1[i+side-1][j-1] -(i!=0)*obs1[i-1][j+side-1]
			side_c[side]=min(count0,count1,side_c[side])
input()
#print(side_c)
#print(*obs0,sep="\n")
#print(*obs1,sep="\n")
list_c=list(map(int,input().split()))
for i in range(len(list_c)):
	c=list_c[i]
	answer=1
	for side in range(2,max_side+1):
		if c<side_c[side]:
			answer=side-1
			break
	if c>=side_c[max_side]:
		answer=max_side
	print(answer)




