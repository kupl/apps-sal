t=int(input())
for _ in range(t):
 n,m=[int(x) for x in input().split()]
 mat=[]
 ans=[]
 for i in range(n+2):
  l=[]
  p=[]
  for j in range(m+2):
   l.append(0)
   p.append(1000000000)
  mat.append(l)
  ans.append(p)
 y=int(input())
 for i in range(y):
  a,b=[int(x) for x in input().split()]
  mat[a][b]=1
  ans[a][b]=0
 y=int(input())
 for i in range(y):
  a,b=[int(x) for x in input().split()]
  mat[a][b]=1000000000
  ans[a][b]=1000000000
 for i in range(1,n+1):
  for j in range(1,m+1):
   if mat[i][j]==1 or mat[i][j]==1000000000:
    continue
   else:
    ans[i][j]=min(ans[i][j],ans[i][j-1]+1,ans[i-1][j]+1)
 for i in range(n,0,-1):
  for j in range(m,0,-1):
   if mat[i][j] == 1 or mat[i][j] == 1000000000:
    continue
   else:
    ans[i][j]=min(ans[i][j],ans[i+1][j]+1,ans[i][j+1]+1)
 for i in range(1,n+1):
  for j in range(m, 0, -1):
   if mat[i][j] == 1 or mat[i][j] == 1000000000:
    continue
   else:
    ans[i][j] = min(ans[i][j], ans[i - 1][j] + 1, ans[i][j + 1] + 1)
 for i in range(n, 0, -1):
  for j in range(1,m+1):
   if mat[i][j] == 1 or mat[i][j] == 1000000000:
    continue
   else:
    ans[i][j] = min(ans[i][j], ans[i + 1][j] + 1, ans[i][j - 1] + 1)
 for i in range(1,n+1):
  for j in range(1,m+1):
   if mat[i][j]==1 or mat[i][j]==1000000000:
    continue
   else:
    ans[i][j]=min(ans[i][j],ans[i][j-1]+1,ans[i-1][j]+1)
 for i in range(n,0,-1):
  for j in range(m,0,-1):
   if mat[i][j] == 1 or mat[i][j] == 1000000000:
    continue
   else:
    ans[i][j]=min(ans[i][j],ans[i+1][j]+1,ans[i][j+1]+1)
 for i in range(1,n+1):
  for j in range(m, 0, -1):
   if mat[i][j] == 1 or mat[i][j] == 1000000000:
    continue
   else:
    ans[i][j] = min(ans[i][j], ans[i - 1][j] + 1, ans[i][j + 1] + 1)
 for i in range(n, 0, -1):
  for j in range(1,m+1):
   if mat[i][j] == 1 or mat[i][j] == 1000000000:
    continue
   else:
    ans[i][j] = min(ans[i][j], ans[i + 1][j] + 1, ans[i][j - 1] + 1)
 for i in range(1,n+1):
  for j in range(1,m+1):
   if mat[i][j]==1000000000:
    print('X',end=" ")
   elif ans[i][j]>=1000000000:
    print('-1',end=" ")
   else:
    print(ans[i][j],end=" ")
  print()
