# 484A

from sys import stdin

__author__ = 'artyom'

n = int(stdin.readline().strip())
for i in range(n):
  l, r = list(map(int, stdin.readline().strip().split()))
  x, p = l, 1
  while 1:
    x |= p
    if x > r:
      break
    p = p << 1 | 1
    l = x

  print(l)
