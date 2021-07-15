def sum_triangular_numbers(n):
  if n<0:
    return 0
  else: 
    c = n*(n+1)*(n+2)//6
    return c

