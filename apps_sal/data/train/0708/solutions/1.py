# cook your dish here
for _ in range(int(input())):
 n,k = list(map(int,input().split()))
 mod = 10**9+7
 s=0
 for i in range(1,n+1):
  p = pow(k,(2*i)-1,mod)
  # print(p)
  s=(s+p)%mod
  # print(k)
  k = (p*k)%mod
 print(s)


