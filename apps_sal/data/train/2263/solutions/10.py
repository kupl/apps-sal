s = input()
n = len(s)
flg = 0
for i in range(1,n):
  if s[i-1] != s[i]:
    flg += 1
if flg == 0:
  print(1)
  return
par = (s.count("a")+s.count("b")*2+2)%3
dp = [[0 for i in range(9)] for j in range(n)]
mod = 998244353
dp[0][0] = 1
dp[0][4] = 1
dp[0][8] = 1
for i in range(1,n):
  dp[i][0] = dp[i-1][5]+dp[i-1][8]
  dp[i][1] = dp[i-1][3]+dp[i-1][6]
  dp[i][2] = dp[i-1][4]+dp[i-1][7]
  dp[i][3] = dp[i-1][1]+dp[i-1][7]
  dp[i][4] = dp[i-1][2]+dp[i-1][8]
  dp[i][5] = dp[i-1][0]+dp[i-1][6]
  dp[i][6] = dp[i-1][0]+dp[i-1][3]
  dp[i][7] = dp[i-1][1]+dp[i-1][4]
  dp[i][8] = dp[i-1][2]+dp[i-1][5]
  for j in range(9):
    dp[i][j] %= mod
ans = pow(3,n-1,mod)-dp[-1][par]-dp[-1][par+3]-dp[-1][par+6]
if flg == n-1:
  ans += 1
if n == 3 and flg == n-1 and par == 2:
  ans -= 1
print(ans%mod)
