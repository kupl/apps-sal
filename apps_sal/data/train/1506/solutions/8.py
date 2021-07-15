n,m=map(int,input().split())
mat=[]
for _ in range(n):
 s=input()
 l=list(map(int,s))
 mat.append(l)
pref=[[0 for _ in range(m+1)] for _ in range(n+1)]
p=[[0 for _ in range(m)] for _ in range(n)]
add=[[0 for _ in range(m)] for _ in range(n)]
for _ in range(int(input())):
 x1,y1,x2,y2=map(int,input().split())
 pref[x1-1][y1-1]+=1
 pref[x2][y1-1]-=1
 pref[x1-1][y2]-=1
 pref[x2][y2]+=1
for i in range(n):
 for j in range(m):
  if i==0:
   p[i][j]=pref[i][j]
  else:
   p[i][j]=p[i-1][j]+pref[i][j]
for i in range(n):
 for j in range(m):
  if j==0:
   add[i][j]=p[i][j]
  else:
   add[i][j]=add[i][j-1]+p[i][j]
for i in range(n):
 for j in range(m):
  mat[i][j]+=add[i][j]
  mat[i][j]%=2
for i in range(n):
 for j in range(m):
  print(mat[i][j],end="")
 print()

