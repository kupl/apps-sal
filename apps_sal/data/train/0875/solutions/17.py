from itertools import chain

R = lambda: list(map(int, input().split()))
t = int(input())
for _ in range(t):
 n, *z = R()
 a = list(R())
 u = set(chain.from_iterable((x, -x) for x in a))
 v = set(x + y for x in z for y in u)
 if 0 in v:
  print(1)
 elif u <= v:
  print(2)
 else:
  print(0)

