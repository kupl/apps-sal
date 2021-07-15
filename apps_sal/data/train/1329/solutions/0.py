T = int(input())
for t in range(T):
 n, m = list(map(int, input().split()))
 c = list(map(int, input().split()))
 dp1 = [1e9]*((1 << n)+1)
 for i in range(n):
  dp1[1 << i] = c[i] 
 
 dp1[1 << (n-1)] = min(dp1[1 << (n-1)], sum(c))
 
 for i in range(m):
  l = list(map(int, input().split()))
  cost = l[0]
  s = l[1]
  items = l[2:]
  mask = 0
  for j in items:
   mask = mask | (1 << (j-1))
  dp1[mask] = min(dp1[mask], cost)
 
 for i in range((1<<n) - 1, -1, -1):
  for j in range(n):
   if i & (1<< j):
    dp1[i ^ (1<<j)] = min(dp1[i ^ (1<<j)], dp1[i])
 
 dp2 = [1e9]*((1 << n) + 1)
 dp2[0] = 0
 for i in range(1 << n):
  submask = i
  while submask > 0:
   dp2[i] = min(dp2[i], dp2[i ^ submask] + dp1[submask])
   submask = (submask-1) & i
 
 print(dp2[(1 << n)-1])

