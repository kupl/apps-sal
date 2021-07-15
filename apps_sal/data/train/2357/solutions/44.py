n,m = list(map(int,input().split()))
A = list(map(int,input().split()))
mod = 10**9+7
s = sum(A)
if s>m:print((0));return
ans = 1
a = 1
for i in range(n+s):
    ans*=m+n-i
    a*=i+1
    ans%=mod
    a%=mod

ans = ans*pow(a,mod-2,mod)
print((ans%mod))

