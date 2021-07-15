# cook your dish here
import math
for _ in range(int(input())):
 N=int(input())
 t=int(math.sqrt(2*N+2))
 if ((t*t+1)<N):
  t=t+1
 if(t&1==1):
  print(N%t)
 else:
  k=N%t
  if(k<t//2):
   print(k+t//2)
  else:
   print(k-t//2)

