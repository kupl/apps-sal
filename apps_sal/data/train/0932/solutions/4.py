def recSolve(a, dp, l, r):
 if(l>r):
  return 0
 if dp[l][r] != 0.0:
  return dp[l][r]
 x = a[l]+ (recSolve(a, dp, l+2, r) + recSolve(a, dp, l+1, r-1))*0.5
 y = a[r]+ (recSolve(a, dp, l+1, r-1) + recSolve(a, dp, l, r-2))*0.5
 dp[l][r] = (x+y)*0.5
 return dp[l][r]
for _ in range(int(input())):
 n = int(input())
 a = list(map(int, input().split()))
 dp = [[0.0]*(n+1) for i in range(n+1)]
 res = recSolve(a, dp, 0, n-1)
 print(res)
