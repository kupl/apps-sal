def numDecodings(s):
 dp = [0] * (len(s) + 2)
 dp[0] = 1
  
 for i in range(len(s)):
  if int(s[i]) != 0:
   dp[i+1] += dp[i]
   
  if int(s[i:i+2]) >= 10 and int(s[i:i+2]) <= 26:
   dp[i+2] += dp[i]
  
 return dp[len(s)] # careful
t=int(input())
for _ in range(t):
 st=input()
 print(numDecodings(st)%1000000007)

