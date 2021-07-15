a=int(input())
for i in range(a):
 m,o=input().split()
 n,k=[int(m),int(o)]
 b=list(map(int,input().split()))
 c=max(b)
 u=0
 z=1
 if k<c:
  print("-1")
 else:
  for j in b:
   if u+j <=k:
    u=u+j
   else:
    u=j
    z=z+1
  print(z)
