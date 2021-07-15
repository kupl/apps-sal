# cook your dish here
for t in range(int(input())):
 n,k,v=[int(x)for x in input().rstrip().split()]
 a=[int(x)for x in input().rstrip().split()]
 sums=(n+k)*v
 b=sums-sum(a)
 if b>0:
  if b%k==0:
   print(b//k)
  else:
   print(-1)
 else:
  print(-1)

