def capitalize(s):
  return next([x, x.swapcase()] for x in [''.join(c if i%2 else c.upper() for i, c in enumerate(s))])
