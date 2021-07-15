def shape_area(n):
  p = 0
  area = 1
  for i in range (1, n):
      p = n*4-4
      n -= 1
      area += p
  return area
  

