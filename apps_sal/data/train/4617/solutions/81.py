def powers_of_two(n):
  num = n
  twopower = 2
  doubles = [1]

  while num > 0:
    doubles.append(twopower)
    num -= 1
    twopower *= 2

  return doubles
