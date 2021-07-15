for _ in range(int(input())):
	N=int(input())
	A=list(map(int,input().split()))
	c=False
	for i in range(N-2):
		if A[i]==A[i+1]==A[i+2]:
			c=True
			break
	if c==False:
		print('No')
	else:
		print('Yes')
