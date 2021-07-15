debug = True

n, q = list(map(int, input().split()))
a = [0] + list(map(int, input().split()))


def small_inputs():
 p = list(map(int, input().split()))

 if p[0] == 1:
  i, k = p[1:]

  c = i
  for j in range(k):
   d = 1
   m = c + 1
   while m <= n and d <= 100:
    if a[m] > a[c]:
     c = m
     break
    d += 1
    m += 1
   if m == n + 1 or d > 100:
    break
  print(c)

 else:
  l, r, x = p[1:]
  for i in range(l, r + 1):
   a[i] += x


def large_inputs():
 p = list(map(int, input().split()))

 if p[0] == 1:
  i, k = p[1:]
  print(-1)

 else:
  l, r, x = p[1:]

for test in range(q):

 if n <= 1000 and q <= 1000:
  small_inputs()
 else:
  large_inputs()

