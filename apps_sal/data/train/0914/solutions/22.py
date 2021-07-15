R = lambda : map(int, input().split())
f = lambda x: ([0] + x, x, x[1:] + [0])

t, = R()
for _ in range(t):
  n, m = R()
  a = b = [0] * m 
  for _ in range(n):
    a = list(map(max, *f(a), *f(b)))
    b = list(R())
    print(''.join('01'[x < y] for x, y in zip(a, b)))

