def matrix_mult(a, b):
  n = len(a)
  x = [[0 for i in range(n)] for j in range(n)]
  
  for k in range(n):
      for i in range(n):
          for j in range(n):
              x[i][j] += a[i][k] * b[k][j]
          
  return x
