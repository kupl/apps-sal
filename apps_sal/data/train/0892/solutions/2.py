def f(c):
  t = s + c
  i = 0
  r = 1
  while i < len(t):
    j = t.rfind(c, i, i + k)
    if j < 0:
      return n 
    r += 1
    i = j + 1
  return r

R = lambda: list(map(int, input().split()))
t, = R()
for _ in range(t):
  n, k = R()
  n += 2
  s = ''.join(f'{x%2}' for x in R())
  print(min(list(map(f, '01'))) % n - 1)

