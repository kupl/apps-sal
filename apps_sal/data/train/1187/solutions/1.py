ts = int(input())
for _ in range(ts):
 n, m = map(int, input().split())
 t, tt, res, cnt = 1, [], 0, 1
 while t <= n:
  t *= m
  v = n // t
  v -= v // m
  if tt:tt[-1] -= v
  tt.append(v)
 for i, v in enumerate(tt):
  res += ((i + 2) // 2) * v
  if i & 1 == 0:
   cnt = cnt * pow((i + 2) // 2 + 1, v, 998244353) % 998244353
 print(n - res, cnt)
