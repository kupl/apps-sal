t=int(input())
for _ in range (t):
 n,k=map(int,input().split())
 d={}
 for i in range(n):
  s,f,p=map(int,input().split())
  try:
   d[p].append((f,s))
  except:
   d[p]=[(f,s)]
 ans=0
 for i in d:
  d[i].sort()
  start=-1
  for j in d[i]:
   if j[1]>=start:
    ans+=1
    start=j[0]
 print(ans)
