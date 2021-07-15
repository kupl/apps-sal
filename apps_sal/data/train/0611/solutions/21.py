from collections import defaultdict
x=int(input())
for __ in range(x):
 n=int(input())
 a=list(map(int,input().split()))
 d=defaultdict(list)
 for i in range(n):
  d[a[i]].append(i)
 b=set(a)
 for i in b:
  c=0
  if len(d[i])>1:
   for j in d[i]:
    if len(d[j+1])>0:
     c+=1
    if c==2:
     break
  if c==2:
   break
 if c==2:
  print("Truly Happy")
 else:
  print("Poor Chef")
