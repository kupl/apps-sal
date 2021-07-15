def nth_floyd(n):
  sum = 0
  for x in range(1,n):
    if sum + x >= n:
        return x
    sum += x
