# cook your dish here
n=int(input())
arr=[int(x) for x in input().split()]
if n<3:
    ans=min(arr)
    print(ans)
else:
    dp=[None for x in range(n)]
    dp[0]=arr[0];dp[1]=arr[1];dp[2]=arr[2]
    for i in range(3,n):
        dp[i]=min(dp[i-1],dp[i-2],dp[i-3])+arr[i]
    print(min(dp[-1],dp[-2],dp[-3]))

