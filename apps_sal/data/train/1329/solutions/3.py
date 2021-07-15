INF=5*(10**6)

def solve():
 dp=[INF]*(1<<18 + 1)
 n,m=list(map(int,input().split()))
 line=list(map(int,input().split()))
 for i in range(n):
  dp[(1<<i)]=line[i]
 for i in range(m):
  line=list(map(int,input().split()))
  c=line[0]
  mask=0
  for j in range(line[1]):
   mask= mask | (1<<(line[2+j]-1))
  dp[mask]=min(dp[mask],c)
 mask=(1<<n)-1
 while mask>=0:
  for j in range(n):
   submask = mask & (1<<j)
   if submask>0:
    dp[mask^(1<<j)]=min(dp[mask^(1<<j)],dp[mask])
  mask-=1
 for _ in range(1):
  for i in range(1<<n):
   submask=(i-1)&i
   while submask>0:
    dp[i]=min(dp[i],dp[submask]+dp[i^submask])
    submask=(submask-1)&i
 print(dp[(1<<n)-1])


t=eval(input())
for _ in range(t):
 solve()

