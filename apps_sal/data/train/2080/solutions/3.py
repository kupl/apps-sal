# 261A

from sys import stdin

__author__ = 'artyom'


def read_int():
  return int(stdin.readline().strip())


def read_int_ary():
  return map(int, stdin.readline().strip().split())


m = read_int()
d = sorted(read_int_ary())[0]
n = read_int()
a = list(reversed(sorted(read_int_ary())))

res = i = 0
while i < n:
  next = i + d
  res += sum(a[i:min(next, n)])
  i = next + 2

print(res)
