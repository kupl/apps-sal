def triangle_type(a, b, c):
  x, y, z = sorted([a, b, c])
  diff = z*z - y*y - x*x
  if z >= x+y: return 0
  elif not diff: return 2
  return 1 if diff < 0 else 3
