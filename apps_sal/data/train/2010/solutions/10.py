n = (int)(input())

h = list(map(int,input().split()))

dp = []

dp.append(1)

for i in range(1,n-1,1):

    dp.append(min(dp[i-1]+1,h[i]))

dp.append(1)

for i in range(n-2,0,-1):

    dp[i]=min(dp[i],dp[i+1]+1)

mx=-1

for i in range(n):

    mx=max(mx,dp[i])

print(mx)





# Made By Mostafa_Khaled

