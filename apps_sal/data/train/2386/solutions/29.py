t=int(input())
for i in range(0,t):
	n=int(input())
	L=list(map(int,input().split()))
	M=[False]*(n+1)
	N=[]
	for i in range(0,2*n):
		if(not M[L[i]]):
			N.append(L[i])
			M[L[i]]=True
	print(*N)
