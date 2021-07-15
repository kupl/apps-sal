# cook your dish here
mod=1000000007
for _ in range(int(input())):
 n,a=list(map(int, input().split()))
 p,ans=1,0
 for i in range(n):
  a1=pow(a, p, mod)
  ans=(ans+a1)%mod
  a=(a*a1)%mod
  p+=2
  
 print(ans)
