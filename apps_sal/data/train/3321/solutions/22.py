def evil(n):
  x = bin(n)
  counts = x.count("1")
  if counts % 2==0:
    return "It's Evil!"
  else:
    return "It's Odious!"
