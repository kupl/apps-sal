import math
for i in range(int(input())):
 n,k=list(map(int,input().split()))
 a=list(map(int,input().split()))
 m=math.ceil(sum(a)/k)
 if k==n:
  print(max(a))
 elif k>=sum(a):
  print(1)
 else:
  for i in range(m,max(a)+1):
   s=0
   for j in a:
    s+=math.ceil(j/i)
   if s<=k:
    print(i)
    break

