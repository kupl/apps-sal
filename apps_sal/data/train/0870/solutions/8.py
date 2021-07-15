import numpy as np
i8 = np.int64


def solve_core(a, n):
 res = 0
 s1 = a[0]
 s2 = a[1]
 s3 = np.sum(a[2::2])
 for i in range(1, n, 2):
  t3 = s3
  for j in range(i + 1, n + 1, 2):
   res = max(res, s1 + s2 + t3)
   s2 += a[j + 1]
   t3 -= a[j]
  s1 += a[i + 1]
  s2 = a[i + 2]
  s3 -= a[i + 1]
 return res


def solve(S):
 N = len(S)
 a = np.zeros(N + 2, i8)
 i = 0
 prev = S[0]
 count = 0
 for c in S:
  if c == prev:
   count += 1
  else:
   a[i] = count
   prev = c
   count = 1
   i += 1
 else:
  a[i] = count
  i += 1
 if i < 4:
  return 0
 else:
  res = max(solve_core(a, i), solve_core(a[1:], i - 1))
  return N - res

def main():
 T = int(input())
 for _ in range(T):
  S = input()
  print(solve(S))

def __starting_point():
 main()
__starting_point()
