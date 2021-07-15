def ii():
 return int(input())
def mi():
 return list(map(int, input().split()))
def li():
 return list(mi())
from collections import deque

for t in range(ii()):
 n, k = mi()
 a = [0] + li()

 def solve(a, k):
  n = len(a)
  dp = [0] * n
  d = deque()
  d.append((0, 0))
  for i in range(1, n):
   if i - d[0][0] > k:
    d.popleft()
   dp[i] = max(d[0][1], a[i] + (dp[i - k - 1] if i >= k + 1 else 0))
   while d and d[-1][1] <= dp[i]:
    d.pop()
   d.append((i, dp[i]))
  return d[0][1]


 odd = solve([x if x % 2 else 0 for x in a], k)
 even = solve([0 if x % 2 else x for x in a], k)
 print(odd + even)

