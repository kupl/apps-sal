import sys
input = sys.stdin.readline
N, M = map(int, input().split())
e = [set([x for x in range(1, N + 1) if i != x]) for i in range(N + 1)]
for _ in range(M):
  u, v = map(int, input().split())
  e[u].discard(v)
  e[v].discard(u)

cl = [0] * (N + 1)
dp = [0] * (N + 1)
dp[0] = 1
for x in range(1, N + 1):
  if cl[x]: continue
  s = [x]
  qs = []
  cl[x] = 1
  while len(s):
    p = s.pop()
    qs.append(p)
    for q in e[p]:
      if cl[q]:
        if cl[q] % 2 == cl[p] % 2:
          print(-1)
          return
        continue
      cl[q] = cl[p] % 2 + 1
      s.append(q)
  predp = dp[: ]
  for i in range(N, -1, -1):
    if dp[i] == 0: continue
    u = 0
    v = 0
    for q in qs:
      u += cl[q] % 2
      v += cl[q] % 2 == 0
    dp[i] -= predp[i]
    dp[i + u] += 1
    dp[i + v] += 1
  #print(dp)
res = N * (N - 1) // 2
for i in range(1, N + 1):
  if dp[i] == 0: continue
  u = i * (i - 1) // 2
  v = (N - i) * (N - i - 1) // 2
  res = min(res, u + v)
print(res)
