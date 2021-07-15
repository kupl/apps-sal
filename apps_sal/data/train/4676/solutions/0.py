def diff(poly):
  return [poly[i] * (len(poly)-1-i) for i in range(len(poly)-1)]
