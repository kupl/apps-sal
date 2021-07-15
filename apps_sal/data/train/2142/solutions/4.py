n=int(input())
A=[0]*n
ans=[0]*n
for i in range(n):
	A[i]=list(map(int,input().split()))
	for j in range(n):
		if(j==i):continue
		ans[i]|=A[i][j]
for i in range(n):
	print(ans[i],' ',end='')

