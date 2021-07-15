R = lambda : map(int, input().split())

t, = R()
for _ in range(t):
  n, m = R()
  b = [0] * m 
  for _ in range(n):
    a = list(R())
    b = list(map(max, a, [0] + b, b, b[1:] + [0]))
    print(''.join('10'[x < y] for x, y in zip(a, b)))

