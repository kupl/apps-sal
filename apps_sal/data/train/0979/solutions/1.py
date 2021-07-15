n, m, k = list(map(int, input().split()))

if k == 1:
 x, y = 0, 0
 for p in range(2, n + 1):
  x += (n - p + 1)
 for p in range(2, m + 1):
  y += (m - p + 1)
 ans = x * y
 x = 0
 for p in range(1, n + 1):
  x += (n - p + 1)
 y = 0
 for p in range(1, m + 1):
  y += (m - p + 1)
 ans += m * x
 ans += n * y
 ans -= n * m
 print(ans)
else:
 x, y = 0.0, 0.0
 q = 1.0
 for p in range(2, n + 1):
  q /= k * k
  x += (n - p + 1) * q
 for p in range(2, m + 1):
  q /= k * k
  y += (m - p + 1) * q
 ans = k * x * y
 x = 0.0
 q = 1.0
 for p in range(1, n + 1):
  x += (n - p + 1) * q
  q /= k
 y = 0.0
 q = 1.0
 for p in range(1, m + 1):
  y += (m - p + 1) * q
  q /= k
 ans += m * x
 ans += n * y
 ans -= n * m
 ans += 1e-9
 # print ans
 print("%.0f" % ans)

