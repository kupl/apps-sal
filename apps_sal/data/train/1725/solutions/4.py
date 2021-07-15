import numpy as np

def pow(mat, n):
  if n == 1: return mat
  mat2 = pow(mat, n//2)
  mat2 = np.dot(mat2, mat2) % 12345787
  if n % 2 == 1: mat2 = np.dot(mat2, mat) % 12345787
  return mat2

def circular_limited_sums(max_n, m):
  mat = np.zeros(shape=(m+1, m+1), dtype=np.int64)
  for a in range(m+1):
    for b in range(m+1):
      if a+b <= m:
        mat[a, b] = 1
  return np.trace(pow(mat, max_n)) % 12345787


