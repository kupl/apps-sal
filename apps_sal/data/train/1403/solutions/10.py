# cook your dish here
t = int(input())
for _ in range(t):
 s = input()
 dp = [0] * (len(s)+1)
 dp[0] = 1
 dp[1] = 1
 for i in range(2,len(s)+1):
  if s[i-1] >'0':
   dp[i] = dp[i-1]
  if s[i-2] == '1' or (s[i-2] == '2' and s[i-1] < '7'):
   dp[i] += dp[i-2]
 
 if s[0] == '0':
  print(0)
 else:
  print(dp[len(s)] % (10**9 + 7))
