n=int(input())
lis=list(map(int, input().split()))
dp=[0]*n
dp[0]=lis[0]
dp[1]=lis[1]
dp[2]=lis[2]
if(n<3):
    print(sum(lis))
    return
for i in range(3 ,len(lis)):
    dp[i]=min(dp[i-1],dp[i-2],dp[i-3])
    dp[i]+=lis[i]
print(sum(lis)-min(dp[n-1], dp[n-2], dp[n-3]))

