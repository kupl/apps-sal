def matrix(L,n,m,c):
 d={}
 dp=[[0]*(m+1)]*(n+1)
 for i in range(1,n+1):
  for j in range(1,m+1):
   if L[i-1][j-1]==c:
    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
   else:
    dp[i][j]=0
   d[dp[i][j]]=1
 return d

from sys import stdin
n,m,q=list(map(int,stdin.readline().split()))
L=[]
for i in range(n):
 L.append(stdin.readline().strip())
male=matrix(L,n,m,'M')
female=matrix(L,n,m,'F')
for i in range(q):
 query=stdin.readline().split()
 if query[1]=='F':
  if female.get(int(query[0]),0)==0:
   print('no')
  else:
   print('yes')
 else:
  if male.get(int(query[0]),0)==0:
   print('no')
  else:
   print('yes')

