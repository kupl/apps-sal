import math
for _ in range(int(input())):
 n=int(input())
 a=[int(x) for x in input().split()]
 res=a[0]
 m=0
 for i in range(1,n):
  res=math.gcd(res,a[i])
  if res==1:
   m=1
   break
 if m==1:
  print(n)
 else:
  print(-1)
