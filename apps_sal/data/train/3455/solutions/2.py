def disarium_number(num):
  total = sum(int(n) ** i for i, n in enumerate(str(num), 1))
  return '{} !!'.format('Disarium' if total == num else 'Not')
