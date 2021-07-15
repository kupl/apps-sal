n,m = map(int,input().split())
a = list(map(int,input().split()))
mod = 10**9+7

s = sum(a)
fact = 1
ans = 1
for i in range(s+n):
    ans *= (m+n-i)
    ans %=mod
    fact *= (i+1)
    fact %= mod
    
ans *= pow(fact,mod-2,mod)
print(ans%mod)
