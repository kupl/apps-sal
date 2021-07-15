from math import sqrt
for _ in range(int(input())):
 n=int(input())
 j=0
 x,y=0,0
 k=0
 while(x!=n):
  j+=1
  if(j<=n):
   x=j
  if(y>=j*j):
   j=int(sqrt(y))
   continue
  if(y+j*j<n*n and x!=n):
   y+=j*j
  else:
   x=n
  k+=1
 print(k)

