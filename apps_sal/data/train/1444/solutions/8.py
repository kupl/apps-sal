try:
	for _ in range(int(input())):
		num=int(input())
		arr=list(map(int,input().split()))
		dp=[0]*num
		dpr=[0]*num
		dpt=[0]*num
		dp[0]=1
		dpr[0]=0
		ans=1
		for i in range(1,num):
			j=i+1
			count=1
			dp[i]=dp[i-1]
			if i-2>=0 and arr[i-2]==2:
				dp[i]+=dp[i-2]
				if i-3>=0 and arr[i-3]==2:
					dp[i]+=dp[i-3]
			if arr[i-1]==2 and i<num-1:
				while j<num and arr[j]==2:
					j+=1
					count+=1
				if j==num:
					dpr[i]=dp[i-1]*(count-1)
				elif count%2!=0:
					if j<num-1 and arr[j+1]==2:
						dpr[i]=dp[i-1]*(count+1)
					else:
						dpr[i]=dp[i-1]*(count)
				elif count%2==0:
					dpr[i]=dp[i-1]*(count-1)
			ans+=dpr[i]+dp[i]
		print(ans)
except:
	pass



			
