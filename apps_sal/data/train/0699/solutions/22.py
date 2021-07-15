import math
t = int(input())
for _ in range(t):
 n, k, d = list(map(int, input().split()))
 total_prob = sum(list(map(int, input().split())))
 nd = math.floor(total_prob / k)
 if total_prob < k:
  print(0)
 else:
  if nd < d:
   print(nd)
  else:
   print(d) 

