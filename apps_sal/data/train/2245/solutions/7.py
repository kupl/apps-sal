from sys import *

rd = lambda: list(map(int, stdin.readline().split()))

n, m, k = rd()
a = rd()
b = [rd() for _ in range(m)]
x = [0]*(m+1)
y = [0]*(n+1)

for _ in range(k):
  l, r = rd()
  x[l-1] += 1
  x[r]   -= 1

s = 0
for i in range(m):
  l, r, d = b[i]
  s += x[i]
  y[l-1] += s*d
  y[r]   -= s*d

s = 0
for i in range(n):
  s += y[i]
  a[i] += s
print(*a)
