def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

def gap(g, m, n):
    x = 0
    y = 0
    for i in range(m,n+1):
      if isPrime(i):
        if x == 0:
          x = i
        elif y == 0:
          y = i
        else:
          x = y
          y = i
      if y - x == g:
        return [x, y]
    return None

