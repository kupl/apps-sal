take=lambda : input().strip()
cal=lambda : list(map(int,take().split()))
from math import sqrt
T=int(take())
for _ in range(T):
 N=take()
 alpha={}
 s=list(cal())
 for i in s:
  if i in alpha:
   alpha[i]+=1
  else:
   alpha[i]=1
 for e in sorted(alpha.keys()):
  print(str(e)+': '+str(alpha[e]))
