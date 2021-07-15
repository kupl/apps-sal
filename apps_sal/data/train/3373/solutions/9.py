def matrix_mult(a, b):
  c = [[0]*len(a) for i in range(len(a))]
  for i in range(len(a)):
      for j in range(len(a)):
          for n in range(len(a)):
              c[i][j]+=a[i][n]*b[n][j]
  return c
