for _ in range(int(input())):
 n,k,l=list(map(int,input().split()))
 if k*l<n or (k==1 and n>1):
  print(-1)
 else:
  d=1
  for i in range(1,n+1):
   if d>k:
    d=1
   print(d,end=" ")
   d+=1
  print()
