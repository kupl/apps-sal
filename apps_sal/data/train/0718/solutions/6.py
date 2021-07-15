t=int(input())
for i in range(t):
 s=0
 r=1
 n=int(input())
 for j in range(0,n+1):
  for k in range(0,j):
   print(s,end=" ")
   p=r+s
   s,r=r,p
  print()
