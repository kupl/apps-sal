def isPrime(n):
  if n <= 3:
    return n > 1
  elif n % 2 == 0 or n % 3 == 0:
    return False
  i = 5

  while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return False
    i += 6
  return True

def gap(g, m, n):
  for i in range(m, n-g+1):
    if isPrime(i) and isPrime(i+g):
      composite = True
      for j in range(i+1, i+g-1):
        if isPrime(j):
          composite = False
          break
      if composite:
        return [i, i+g]
  return None
