def is_triangle(a, b, c):
  sides = (a, b, c)
  sides = sorted(sides)
  c = sides[-1]
  b = sides[1]
  a = sides[0]
  return c < a + b
