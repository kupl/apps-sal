from collections import defaultdict
x,y=list(map(int,input().split()))
m=[]
p=defaultdict(list)
for __ in range(x):
 a=list(map(int,input().split()))
 b=list(map(int,input().split()))
 c=defaultdict()
 for i in range(y):
  c[a[i]]=b[i]
 a.sort()
 d=[]
 for i in range(y):
  d.append(c[a[i]])
 n=0
 for i in range(1,y):
  if d[i]<d[i-1]:
   n+=1
 m.append(n)
 p[n].append(__ + 1)
m.sort()
m=list(set(m))
for i in m:
 if len(p[i])>1:
  p[i].sort()
  for j in p[i]:
   print(j)
 else:    
  print(*p[i])

