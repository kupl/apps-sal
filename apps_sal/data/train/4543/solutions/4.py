def shades_of_grey(n):
  n = min(n, 254)
  return ['#'+format(i, '02x')*3 for i in range(1, n+1)]
