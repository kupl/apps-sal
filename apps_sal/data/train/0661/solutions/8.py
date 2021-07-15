import math as m
import cmath as c

t, x = map(int, input().split())
for _ in range(t):
 n = int(input())
 if n >= 0:
  s = m.floor(m.sqrt(n))
 else:
  p = n+0j
  s = c.sqrt(p)
  s = m.floor(s.real)
 if n-(s*s) <= 0.01*x*n:
  print("yes")
 else:
  print("no")
