#=''
import sys
input=sys.stdin.readline
n=int(input())
l=input().split()
li=[int(i) for i in l]
if(n==1):
    print(0)
    return
if(n==2):
    print(min(li))
    return
if(n==3):
    li.sort()
    print(li[0]+li[1])
    return
z=list(li[1:])
ans=li[0]
k=len(z)
dp=[[0 for i in range(2)]for i in range(k)]
dp[0][1]=z[0]
dp[1][0]=z[0]
dp[1][1]=z[1]
for i in range(2,k):
    dp[i][0]=z[i-1]+min(dp[i-2][0],dp[i-2][1])
    dp[i][1]=z[i]+min(dp[i-1][0],dp[i-1][1])
ans=ans+min(dp[-1][0],dp[-1][1])
z=list(li[2:-1])
ok=li[1]+li[-1]
k=len(z)
if(k>=2):
    dp=[[0 for i in range(2)]for i in range(k)]
    dp[0][1]=z[0]
    dp[1][0]=z[0]
    dp[1][1]=z[1]
    for i in range(2,k):
        dp[i][0]=z[i-1]+min(dp[i-2][0],dp[i-2][1])
        dp[i][1]=z[i]+min(dp[i-1][0],dp[i-1][1])
    ok=ok+min(dp[-1][0],dp[-1][1])
print(min(ans,ok))

