t=int(input())
while t:
 n=int(input())
 a=[int (o) for o in input().split()]
 b=[int (o) for o in input().split()]
 a.sort()
 b.sort()
 s=0
 if a[0]==a[n-1] and b[0]==b[n-1]:
  print(n*min(a[0],b[0]))
 else:
  for i in range(n):
   s+=min(a[i],b[i])
  print(s)
 t-=1

