def matrix_mult(a, b):
  C = []
  for i in range(len(a)):
      row=[]
      for j in range(len(a)):
          z=0
          for k in range(len(a)):
              z += a[i][k]*b[k][j]
          row.append(z)     
      C.append(row)
  return C
