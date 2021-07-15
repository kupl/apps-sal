n,k=map(int,input().split())
dp=[[0]*k for i in range(n)]
for i in range(n):
 dp[i]=[int(x) for x in input().split()]
#print(dp)
sumr=[0]*n
for i in range(n):
 sumr[i]=sum(dp[i])
#print(sumr)
for i in range(k):
 for j in range(n):
  if j==0:
   prev=dp[0][i]/sumr[0]
  else:
   curr=(prev)*(dp[j][i]+1)/(sumr[j]+1)+(1-prev)*dp[j][i]/(sumr[j]+1)
   prev=curr
 print(prev,end=" ")

