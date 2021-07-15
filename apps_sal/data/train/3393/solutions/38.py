import math
sqrt = math.sqrt

def getDivisors(x):
  result = []
  i = 1
  while i*i <= x:
    if x % i == 0:
      result.append(i**2)
      if x/i != i:
        result.append((x/i)**2)
    i += 1
  return (result)

def isSquaredDivisor(n):
  squaredList = getDivisors(n)
  sumList = sum(squaredList)
  if sqrt(sumList) % 1 == 0:
    return [n,sumList]
  else:
    return 0

def list_squared(m, n):
  retList = []
  for i in range(m,n+1):
    res = isSquaredDivisor(i)
    if res != 0:
      retList.append(res)
  return retList
