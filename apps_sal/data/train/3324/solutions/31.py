def sale_hotdogs(n):
  price = 0
  if n < 5:
    price = n * 100
  elif n >= 5 and n < 10:
    price = n * 95
  elif n >= 10:
    price = n * 90
  return price
