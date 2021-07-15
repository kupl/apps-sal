import sys
n,m=map(int,input().split())
dp=[[0 for j in range(m+2)] for k in range(n+2)]
a=[]
for j in range(n):
 t=sys.stdin.readline().strip()
 a.append(list(t))
q=int(input())
for j in range(0,q):
 x1,y1,x2,y2=map(int,sys.stdin.readline().split())
 dp[x1][y1]+=1
 dp[x2+1][y2+1]+=1
 dp[x1][y2+1]-=1
 dp[x2+1][y1]-=1
#print(dp)
for j in range(1,n+1):
 for k in range(1,m+1):
  dp[j][k]=dp[j][k]+dp[j-1][k]+dp[j][k-1]-dp[j-1][k-1]
  #print(dp[j][k],a[j-1][k-1])
  if dp[j][k]%2!=0:
   a[j-1][k-1]=int(a[j-1][k-1])^1
for j in range(n):
 print(''.join(map(str,a[j])))
