def find_unknown_number(x, y, z):
  return next(n for n in range(1, int(1e8)) if n%3 == x and n%5 == y and n%7 == z)
