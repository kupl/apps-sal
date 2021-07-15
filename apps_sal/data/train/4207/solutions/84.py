def sum_cubes(n):
  sum = 0
  for number in range(1,n + 1):
    cube = number ** 3
    sum += cube
  return sum
