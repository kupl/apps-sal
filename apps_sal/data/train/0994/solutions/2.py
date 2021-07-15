for _ in range(int(input())):
 n,X=map(int,input().split())
 b=list(map(int,input().split()))
 a=[[0 for j in range(n+1)] for k in range(n+1)]
 for i in range(n):
  for j in range(n):
   a[i+1][j+1]=b[i]+b[j]
 c=0
 #print(a)
 for i in range(n+1):
  for j in range(n+1):
   if i>0:
    a[i][j]+=a[i-1][j]
   if j>0:
    a[i][j]+=a[i][j-1]
   if i>0 and j>0:
    a[i][j]-=a[i-1][j-1]
   ii=i-1; jj=j-1
   while ii>-1 and jj>-1:
    if a[i][j]-a[ii][j]-a[i][jj]+a[ii][jj]==X:
     c+=1
    ii-=1; jj-=1
 #print(a)
 print(c)
