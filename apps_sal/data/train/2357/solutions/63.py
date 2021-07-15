n,m=map(int, input().split())
*a,=map(int, input().split())
mod=10**9+7
l,r=1,1
for i in range(n+sum(a)):
    l,r=l*(n+m-i)%mod,r*(i+1)%mod
print(l*pow(r,mod-2,mod)%mod)
