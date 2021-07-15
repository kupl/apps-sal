t= int (input())
while t:
 dim=input().split()
 n=int(dim[0])
 m=int(dim[1])
 a=[]
 for i in range(n):
  temp=[]
  s=input()
  for j in range(m):
   temp.append(int(s[j]))
  a.append(temp)
 res=[[0 for i in range(m)]for j in range(n)]
 row=[0]*n
 col=[0]*m
 for i in range(n):
  for j in range(m):
   if a[i][j]==1:
    row[i]=1
    col[j]=1
 r=0
 c=0
 for i in range(n):
  if row[i]==0:
   r+=1
 for j in range(m):
  if col[j]==0:
   c+=1
  
 for i in range(n):
  for j in range(m):
   if r==n and c==m:
    res[i][j]=-1
   elif a[i][j]==1:
    res[i][j]=0
   elif row[i]==1 or col[j]==1:
    res[i][j]=1
   else:
    res[i][j]=2
 for i in range(n):
  for j in range(m):
   print(res[i][j],end=' ')
  print()
 t-=1
