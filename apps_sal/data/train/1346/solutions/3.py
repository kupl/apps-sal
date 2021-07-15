# cook your dish here

mod=10**9+7

def power10(N):
 if N==0:
  return dp[0]
 if N%2==1:
  dp[N]=(10*power10(N-1))%mod
  return((10*power10(N-1))%mod)
 else:
  if dp[N//2]==-1:
   dp[N//2]=power10(N//2)%mod
  dp[N]=(dp[N//2]**2)%mod
  return(dp[N]%mod)

from sys import stdin, stdout
T=int(input().strip())

for _ in range(T):
 N,W=map(int,input().strip().split())
 dp=[-1]*(N+1)
 dp[0]=1
 if W>8 or W<-9:
  print(0)
 else:
  if W>=0:
   res=(9-W)*power10(N-2)
  else:
   res=(W+10)*power10(N-2)
  print(res%mod)
