def min_value(digits):
  r=0
  for n in sorted(list(set(digits))): r=r*10+n
  return r
