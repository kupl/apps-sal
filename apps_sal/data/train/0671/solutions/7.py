for _ in range(int(input())):
 n,s = list(map(int,input().split()))
 p = list(map(int,input().split()))
 l = list(map(int,input().split()))

 mo=10000000
 mz=10000000
 for i in range(len(l)):
  if l[i]==0:
   if p[i]<mz:
    mz=p[i]
  else:
   if p[i]<mo:
    mo=p[i]
 ans =s+mo+mz
 if ans<=100:
  print("yes")
 else:
  print("no")
  
   

