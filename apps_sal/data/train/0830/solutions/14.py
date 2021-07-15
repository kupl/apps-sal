from collections import defaultdict
def fn(a,b,n):
 l=[]
 da=defaultdict(lambda:[])
 db=defaultdict(lambda:[])
 idx=jdx=0
 for i,j in zip(a,b):
  if i<j or j not in a:
   print(-1)
   return
  da[i].append(idx)
  db[j].append(jdx)
  idx+=1
  jdx+=1
 c=0
 #print(b)
 while a!=b:
  mx=max(db)
  tc=[da[mx][0]]
  for i in db[mx]:
   if a[i]!=b[i]:
    tc.append(i)
    da[a[i]].remove(i)
    a[i]=mx
    da[mx].append(i)

  del db[mx]
  #print(a)
  l.append(tc)
  c+=1
 print(c)
 for i in range(c):
  print(len(l[i]),end=' ')
  for j in l[i]:
   print(j,end=' ')
  print()




t=int(input())
for i in range(t):
 n=int(input())
 a=input()
 a=[i for i in a]
 b=input()
 b=[i for i in b]
 fn(a,b,n)

