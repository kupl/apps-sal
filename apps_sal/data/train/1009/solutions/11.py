import math
MAX = 10001

def func(ind,g,n,dp,l):
 if ind==n:
  if g==1:
   return 1
  else:
   return 0
 
 if dp[ind][g]!=-1:
  return dp[ind][g]
 
 ans = func(ind+1,g,n,dp,l)+func(ind+1,math.gcd(g,l[ind]),n,dp,l)
 
 dp[ind][g]=ans
 return dp[ind][g]

for _ in range(int(input())):
 n = int(input())
 l = list(map(int,input().split()))
 dp = [[-1 for _ in range(MAX)]for _ in range(n)]
 
 count = 0
 for i in range(n):
  count+=func(i+1,l[i],n,dp,l)

  
 print(count)
