n,r1,r2,r3,d=map(int,input().split())
a=list(map(int,input().split()))
if 2*r1<r3:
  save=[r3-2*r1]*n
else:
  save=[0]*n
for i in range(n):
  save[i]=max(save[i],a[i]*r1+r3-r2-r1)
ans=(n-1)*d+sum(a)*r1+n*r3
dp=[0,0]
for i in range(n):
  dp0=dp[1]
  dp1=dp[1]
  if i+1<n and save[i]+save[i+1]>2*d:
    dp1=max(dp1,dp[0]+save[i]+save[i+1]-2*d)
  if i==n-1:
    dp1=max(dp1,dp[0]+save[i]-2*d)
  if i==n-2:
    dp0=max(dp0,dp[0]+save[i]-d)
  dp1=max(dp1,dp0)
  dp=[dp0,dp1]
print(ans-max(dp0,dp1))
