for _ in range(int(input())):
	num=int(input())
	arr=list(map(int,input().split()))
	dp=[0]*len(arr)
	dpr=[0]*len(arr)
	dpt=[0]*len(arr)
	dp[0]=1
	dpr[0]=0
	ans=1
	for i in range(1,len(arr)):
		j=i+1
		count=1
		dp[i]=dp[i-1]
		if i-2>=0 and arr[i-2]==2:
			dp[i]+=dp[i-2]
			if i-3>=0 and arr[i-3]==2:
				dp[i]+=dp[i-3]
		ans+=dp[i]
		if arr[i-1]==2 and i<len(arr)-1:
			while j<len(arr) and arr[j]==2:
				j+=1
				count+=1
			if j==len(arr):
				ans+=dp[i-1]*(count-1)
			elif count%2!=0:
				if j<len(arr)-1 and arr[j+1]==2:
					ans+=dp[i-1]*(count+1)
				else:
					ans+=dp[i-1]*(count)
			elif count%2==0:
				ans+=dp[i-1]*(count-1)
	print(ans)




			
