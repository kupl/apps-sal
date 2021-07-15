T = int(input())
for _ in range(T):
 p,n=map(int,input().split())
 mod = 1000000007
 if p == 2:
  print(n)
 else:
  f=n
  t=n
  for i in range(p-2):
   f=(f%mod*n)%mod
   a=(f-t+mod)%mod
   t=a
  print(a)
