from functools import lru_cache
n,a,b,c,d=map(int,input().split())

mod=10**9+7
fac=[1]*(n+3)
finv=[1]*(n+3)

t=1
for i in range(1,n+1):
    t*=i
    t%=mod
    fac[i]=t
t=1
for i in range(1,n+1):
    t*=pow(i,mod-2,mod)
    t%=mod
    finv[i]=t

finvp = [finv]
for i in range(n-1):
    p=finvp[-1]
    q=[p[i]*finv[i]%mod for i in range(n+1)]
    finvp.append(q)

dp = [[0 for _ in range(n+1)] for _ in range(b+1)]
dp[a-1][0] = 1

for i in range(a-1,b):
    for j in range(n+1):
        dp[i+1][j]=dp[i][j]
        for k in range(c,1+min(d,j//(i+1))):
            x=j-k*(i+1)
            dp[i+1][j]+=fac[j]*finv[x]*finvp[k-1][i+1]*finv[k]*dp[i][x]%mod
        dp[i+1][j]%=mod
print(dp[b][n])
