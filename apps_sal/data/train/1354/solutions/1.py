mod=1000000007
fact=[1]
for i in range(1,200):
 fact.append((fact[-1]*i)%mod)
def ncr(n,r):
 if n<r:
  return 0
 return (((fact[n]*pow(fact[n-r],mod-2,mod))%mod)*pow(fact[r],mod-2,mod))%mod

for _ in range(eval(input())):
 n,k=list(map(int,input().split()))
 for i in range(n-1):
  u,v=list(map(int,input().split()))
 res=0
 for i in range(1,k+1):
  res+=(((ncr(k,i)*ncr(n-1,i-1))%mod)*fact[i])%mod
  res%=mod
 print(res)


