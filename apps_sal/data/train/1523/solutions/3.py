# cook your dish here
n=int(input())
arr=list(map(int,input().split()))
dp=[0]*(n+1)
dp[0]=0
dp[1]=arr[0]
dp[2]=arr[0]+arr[1]
dp[3]=max(arr[2]+arr[0],arr[1]+arr[2],dp[-1])

for i in range(4,n+1):
    dp[i]=max(dp[i-1],arr[i-1]+dp[i-2],arr[i-1]+arr[i-2]+dp[i-3])
# print(dp)/
print(dp[-1])
# if N > 0:
#     sum[0] = Ps[0]
# if N > 1:
#     sum[1] = Ps[0] + Ps[1]
# if N > 2:
#     sum[2] = max(Ps[0] + Ps[2], max(sum[1], Ps[1] + Ps[2]))


# for i in range(3, N):
#     sum[i] = max(sum[i-2] + Ps[i], max(sum[i-1], sum[i-3] + Ps[i-1] + Ps[i]))

