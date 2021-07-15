t=int(input())
mod=10**9+7
for _ in range(t):
 n,m=map(int,input().split())
 same=[0]
 diff=[m]
 for i in range(n-1):
  s=diff[-1]
  d=(same[-1]+diff[-1])*(m-1)
  same+=[s%mod]
  diff+=[d%mod]
 print((same[-1]+diff[-1])%mod)
