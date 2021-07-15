from math import sqrt, ceil
n = int(input())

n_sqrt = int(ceil(sqrt(n)))
ans = []
i = 1
while i <= n:
  ans = ans + list(range(i, min(i+n_sqrt, n+1)))[::-1]
  i += n_sqrt
print(" ".join(map(str, ans)))


