# cook your dish here
from math import gcd 

t = int(input())
for _t in range(t):
 n = int(input())
 arr = [int(x) for x in input().split()]
 dp = [[0]*10001 for i in range(n)]
 dp[0][arr[0]], sett = 1, set([arr[0]])
 for i in range(1, n):
  dp[i][arr[i]]+=1
  tmp = []
  for j in sett:
   dp[i][j] += dp[i-1][j]
   dp[i][gcd(j, arr[i])] += dp[i-1][j]
   tmp.append(gcd(j, arr[i]))
  sett.update(tmp)
  sett.add(arr[i])
 print(dp[n-1][1])
