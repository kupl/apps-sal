a=int(input())
for i in range(a):
 m,o=input().split()
 n,k=[int(m),int(o)]
 b=list(map(int,input().split()))
 u=0
 z=1
 for j in b:
  if j>k:
   z=0
   break
  elif u+j <=k:
   u=u+j
  else:
   u=j
   z=z+1

 if z==0:
  print(-1)
 else:
  print(z)
