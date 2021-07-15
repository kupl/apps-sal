
n,m= map(int,input().split())
MX=list()
for i in range(n):
 YYY=str(input())
 yy=list(YYY)
 a=[]
 for j in range(m):
  a.append(yy[j])
 MX.append(a)

q=int(input())
dp=[[0 for i in range(m)]for i in range(n)]
for _ in range(q):
 x,y,x2,y2=map(int,input().split())
 dp[x-1][y-1]+=1
 if x2<n:
  dp[x2][y-1]-=1
 if y2<m:
  dp[x-1][y2]-=1
 if x2<n and y2<m:
  dp[x2][y2]-=1


for i in range(n):
 for j in range(1,m):
  dp[i][j]+=dp[i][j-1]

for i in range(m):
 for j in range(1,n):
  dp[j][i]+=dp[j-1][i]

# print(dp)
# print(MX)
for i in range(n):
 for j in range(m):
  if dp[i][j]%2==1:
   if MX[i][j]=='0':
    MX[i][j]='1'
   else:
    MX[i][j]='0'

  

for i in range(n):
 for j in range(m):
   print(MX[i][j],end="")

 print()

