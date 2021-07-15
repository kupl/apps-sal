from collections import defaultdict
from operator import itemgetter
for _ in range(int(input())):
 n=int(input())
 d=defaultdict(list)
 for i in range(n):
  x,y=list(map(int,input().split( )))
  if not d[x]:
   d[x].append(y)
  else:
   d[x][0]=max(d[x][0],y)
 y=[]
 for v in d:
  y.extend(d[v])
 #print(y)
 if len(y)>=3:
  v1=max(y)
  y.remove(v1)
  v2=max(y)
  y.remove(v2)
  v3=max(y)
  y.remove(v3)
  print(v1+v2+v3)
 else:
  print(0)

