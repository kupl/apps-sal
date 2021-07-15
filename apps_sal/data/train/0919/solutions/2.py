t = int(input())
for _ in range(t):
 n = int(input())
 arr = list(map(int, input().split()))
 dp = [-1]*(n+1)
 dp[0] = 0
 for e in arr:
  even=dp[0]
  odd=dp[e]
  dp[e]=max(odd,even+1)
  dp[0]=max(even,odd+1)
 print(n-dp[0])

