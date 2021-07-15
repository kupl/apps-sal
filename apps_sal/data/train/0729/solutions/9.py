for _ in range(int(input())):
 n,m=list(map(int,input().split()))
 dp=[[0 for i in range(m)]for i in range(n)]
 f=0
 mat=[]
 for i in range(n):
  l=list(input())
  l=[int(i) for i in l]
  mat.append(l)
  if 1 in l:
   f=1 
 if f==0:
  for i in range(n):
   z=[-1]*m 
   print(*z)
 else:
  bad_row=set()
  bad_col=set()
  for i in range(n):
   for j in range(m):
    if mat[i][j]==1:
     dp[i][j]=0
     bad_row.add(i)
     bad_col.add(j)
  for i in bad_row:
   for j in range(m):
    if mat[i][j]!=1:
     dp[i][j]=1 
  for j in bad_col:
   for i in range(n):
    if mat[i][j]!=1:
     dp[i][j]=1 
  for i in range(n):
   for j in range(m):
    if i not in bad_row and j not in bad_col:
     dp[i][j]=2 
  for i in range(n):
   print(*dp[i])
   

