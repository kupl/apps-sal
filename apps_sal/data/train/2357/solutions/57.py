# 場合の数をmodで割った余り nCr % mod
def ncr_mod(n,r,mod):
  a,b=1,1
  for i in range(r):
    a*=n-i
    a%=mod
    b*=i+1
    b%=mod
  return (a*pow(b,mod-2,mod))%mod
n,m=map(int,input().split())
a=list(map(int,input().split()))
mod=10**9+7
ans=ncr_mod(m+n,sum(a)+n,mod)
print(ans)
