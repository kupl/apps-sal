for _ in range(int(input())):
 n=int(input())
 st=0
 for i in range(1,n+1):
  st=st+i
  l=[st]
  k=st
  for j in range(i,n+i-1):
   if j < n:
    x=k+j
   else:
    x=k+(2*n-j-1) 
   l.append(x)
   k=x 
  print(*l)
