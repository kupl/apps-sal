# cook your dish here
from collections import Counter
def solve(arr, n, k):
 ans = 0
 dict1 = {}
 mod = 1000000007
 
 for i in range(n):
  if arr[i] in dict1:
   dict1[arr[i]] += 1 
  else:
   dict1[arr[i]] = 1
 l1 = [0]+list(dict1.keys())
 v = min(k, len(l1))
 dp = [[0 for _ in range(v+1)]for _ in range(len(l1))]
 dp[0][0] = 1
 for i in range(1, len(l1)):
  dp[i][0] = 1
  for j in range(1, v+1):
   dp[i][j] = dp[i-1][j] + dp[i-1][j-1]*dict1[l1[i]]
 for i in range(v+1):
  ans += dp[len(l1)-1][i]
  ans = ans%mod
 return ans
 

(n, k) = list(map(int, input().strip().split()))
arr = list(map(int, input().strip().split()))
print(solve(arr, n, k))
