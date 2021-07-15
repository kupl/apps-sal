def spinning_rings(inner_max, outer_max):
  i = 1
  while -(i%(-inner_max - 1)) != i%(outer_max + 1):
      i += 1
  return i
