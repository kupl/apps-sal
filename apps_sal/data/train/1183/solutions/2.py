for t in range(int(input())):
	n=int(input())
	a=list(map(int,input().split()))
	k=int(input())
	dp=[0]*n
	if (a[0]==k):
		dp[0]=1
	for i in range(1,n):
		if (a[i]==k):
			dp[i]=dp[i-1]+1
		else:
			dp[i]=dp[i-1]
	dp_index=n
	for q in range(int(input())):
		x=int(input())
		if (x==0):
			print(dp[-1], end=' ')
		else:
			print(dp[-1]-dp[x-1], end=' ')
		print(n-x, end=' ')
		if (x<dp_index):
			print(dp_index-x+1)
			dp_index=x
		else:
			print(1)
