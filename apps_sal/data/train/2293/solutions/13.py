import sys
input = sys.stdin.readline
N = int(input())
a = list(map(int, input().split()))
zeta = a[: ]
zeta2 = [0] * (1 << N)
for i in range(N):
  for j in range(1 << N):
    if (1 << i) & j:
      if zeta[j] < zeta[(1 << i) ^ j]:
        zeta2[j] = max(zeta[j], zeta2[(1 << i) ^ j])
        zeta[j] = zeta[(1 << i) ^ j]
      elif zeta2[j] < zeta[(1 << i) ^ j]:
        zeta2[j] = zeta[(1 << i) ^ j]

res = 0
for i in range(1, 1 << N):
  res = max(res, zeta[i] + zeta2[i])
  print(res)
