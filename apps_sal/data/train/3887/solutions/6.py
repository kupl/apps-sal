get_r = lambda y: str((y) % 10)
def pattern(n):
  if n < 2: return '' if n < 1 else '1'
  l, r = ''.join(map(get_r, range(1, n))), ''.join(map(get_r, range(n - 1, 0, -1)))
  top = [' ' * (n - 1) + get_r(x) * n + ' ' * (n - 1) for x in range(1, n)]
  return '\n'.join(top) + '\n' + (l + get_r(n) * n + r + '\n') * n + '\n'.join(list(reversed(top)))
