from sys import stdin
input=stdin.readline
for _ in range(int(input())):
    n,k=map(int,input().split())
    s=list(input())
    ans=10**9
    a=['R','G','B']
    for l in range(3):
        x=l
        dp=[0]*(n+1)
        cnt=10**9
        for i in range(n):
            if s[i]!=a[x]:
                dp[i+1]=dp[i]+1
            else: dp[i+1]=dp[i]
            x=(x+1)%3
        for i in range(1,n-k+2):
            cnt=min(cnt,dp[i+k-1]-dp[i-1])
        ans=min(cnt,ans)
    print(ans)
