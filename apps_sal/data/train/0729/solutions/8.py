for _ in range(int(input())):
 x,y=map(int,input().split())
 l=[[int(x) for x in input().strip()] for y in range(x)]
 ans=[[2]*y for k in range(x)]
 temp=0
 rows=set()
 col=set()
 for i in range(x):
  for j in range(y):
   if l[i][j]==1:
    temp=1
    rows.add(i)
    col.add(j)
    ans[i][j]=0
 for ii in rows:
  for var in range(y):
   if ans[ii][var]==2:
    ans[ii][var]=1
 for jj in col:
  for var in range(x):
   if ans[var][jj]==2:
    ans[var][jj]=1

 if temp==0:
  ans=[[-1]*y for k in range(x)]
 for li in ans:
  print(*li)
