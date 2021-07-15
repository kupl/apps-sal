from pprint import *
def modpow(a,n,p):
    if n==0:
        return 1
    x=modpow(a,n//2,p)
    x=(x*x)%p
    if (n%2)==1:
        x=(x*a)%p
    return x%p
def modinv(a,p):
    return modpow(a,p-2,p)
N,K=list(map(int,input().split()))
p=998244353
dp=[[-1 for _ in range(N+1)] for _ in range(N+1)]
for i in range(N+1):
    dp[i][i]=1
for i in range(1,N+1):
    dp[i][0]=0
for i in range(1,N+1):
    for j in range(0,i):
        dp[j][i]=0
#pprint(dp)
for i in range(1,N+1):
    for j in range(N,0,-1):
        #print(i,j)
        if dp[i][j]==-1:
            if 2*j<=i:
                dp[i][j]=(dp[i-1][j-1]+dp[i][2*j])%p
            else:
                dp[i][j]=dp[i-1][j-1]%p
        #pprint(dp)
print((dp[N][K]))

