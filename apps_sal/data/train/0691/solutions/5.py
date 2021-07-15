import sys
from math import sqrt
input = sys.stdin.readline
t = int(input())
for _ in range(t):
 n = int(input())
 a = list(map(int, input().strip().split()))
 max_star = [0] * (10 ** 6 + 5)
 ans = 0
 for i in range(n):
  x = a[i]
  if i > 0:
   ans = max(ans, max_star[x])
  for j in range(1, int(sqrt(x))+1):
   if x % j == 0:
    tempnum = int(x / j)
    if j != tempnum:
     max_star[j] += 1
     max_star[tempnum] += 1
    else:
     max_star[j] += 1
 print(ans)
