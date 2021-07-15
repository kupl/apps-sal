def two_count(n):
  i = 0
  while True:
      n, r = divmod(n, 2)
      if r:
          break
      i += 1
  return i

