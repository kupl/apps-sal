def pattern(n):
  return '\n'.join([''.join(map(str, list(range(n, x, -1)))) for x in range(n)])

