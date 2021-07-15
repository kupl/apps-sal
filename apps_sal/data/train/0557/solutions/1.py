# cook your dish here
import math
for _ in range(int(input())):
 n,m=list(map(int,input().split()))
 p=[10]*n
 for i in range(m):
  l=list(map(int,input().split()))
  i=l[0]-1
  j=l[1]
  k=l[2]
  for s in range(i,j,1):
   p[s]=p[s]*k
 sup=sum(p)
 sup=math.floor(sup/n)
 print(sup)

