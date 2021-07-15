n = int(input())
a = 2
for i in range(1, n + 1):
  b = (i * (i + 1)) * (i * (i + 1))
  assert (b - a) % i == 0, str(i)
  c = (b - a) // i
  print(c)
  a = i * (i + 1)

