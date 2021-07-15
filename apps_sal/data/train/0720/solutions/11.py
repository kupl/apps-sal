
t = int(input())
for k in range(t):
 s = input().strip()
 n = len(s)
 dp = [0]
 for i in s:
  if i == '1':
   dp.append(dp[-1]+1)
  else:
   dp.append(dp[-1])
 d = 1
 ans = 0
 l = 2
 while l <= n:
  i = 0
  while i <= n - l:  # for i in range(0, n - l + 1):
   if dp[i+l] - dp[i] == d:
    ans += 1
    i += 1
   else:
    i += abs(d - (dp[i+l] - dp[i]))
  d += 1
  l = d * d + d
 print(ans)

