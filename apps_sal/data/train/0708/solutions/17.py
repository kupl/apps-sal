def pingalapower(a,n,mod):
 if n==1:
  return a
 x=pingalapower(a,n//2,mod)
 if n%2==0:
  return (x*x)%mod
 else:
  return (x*x*a)%mod
for _ in range(int(input())):
 n,a=map(int,input().split())
 c=1
 ans=0
 mod=10**9+7
 for i in range(n):
  t_1=(pingalapower(a,c,mod)%mod)
  ans=(ans+t_1)%mod
  a=(a*t_1)%mod
  c+=2
 
 print(ans%mod)
