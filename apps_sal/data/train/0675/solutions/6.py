import math
for _ in range(int(input())):
 n=int(input())
 a=[ ]
 b=[2,3,1,5,4]
 for i in range(18):
  a.append(i)
 t=math.log(n,2)
 if t in a:
  print(-1)
 else:
  if n==3:
   print(1,3,2)
  elif n==5:
   print(2,3,1,5,4)
  else:
   for i in range(6,n+1):
    b.append(i)
   i=5
   while i<n:
    t1=math.log(b[i],2)
    if t1 in a:
     b[i],b[i+1]=b[i+1],b[i]
     if i==(n-2):
      break
     else:
      i+=1
    i+=1
   print(*b)
