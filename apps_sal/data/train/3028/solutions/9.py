def factorial(n):

  if n >= 0:
    fact = 1
    for i in range(2, n+1):
      fact *= i
    return fact
  else:
    return None
