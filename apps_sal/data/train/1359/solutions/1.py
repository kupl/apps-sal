for _ in range(int(input())):
 n=int(input())
 a=list(map(int,input().split()))
 ce=co=0
 if n==1:
  print(n-1)
 else:
  for i in a:
   if i%2==0:
    ce+=1
   else:
    co+=1
  if ce==0 or co==0:
   print(n)
  else:
   c1=max(co,ce)
   c2=min(co,ce)
   print(c1+2*(c2-1))
