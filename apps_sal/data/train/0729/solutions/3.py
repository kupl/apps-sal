t=int(input())
for _ in range(t):
 n,m=list(map(int,input().split()))
 d={}
 e={}
 l=[]
 for i in range(n):
  d[i]=0
 for i in range(m):
  e[i]=0
 for i in range(n):
  l.append(input())
 for i in range(n):
  for j in range(m):
   if l[i][j]=='1':
    d[i]=1
    e[j]=1
 ans=[]
 if sum(d.values())+sum(e.values())==0:
  k=[-1]*m
  for i in range(n):
   print(*k)
 else:
  ans=[]
  for i in range(n):
   ans.append([0]*m)
  for i in range(n):
   for j in range(m):
    if l[i][j]=='1':
     ans[i][j]=0
    else:
     if d[i] or e[j]:
      ans[i][j]=1
     else:
      ans[i][j]=2
  for i in range(n):
   print(*ans[i])
     
 

