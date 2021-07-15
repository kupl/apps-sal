def multiples(m, n):
  if type(m) == 'float':
    return []
  return [x * n for x in range(1, m + 1)]
