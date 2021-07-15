def meters(x):
  units = [('Y', 24), ('Z', 21), ('E', 18), ('P', 15), ('T', 12), ('G', 9), ('M', 6), ('k', 3), ('', 0)]
  return next(f'{str(x / 10 ** p).replace(".0", "")}{u}m' for u, p in units if x // 10 ** p >= 1)
