def add(*args):
  return round(sum( v / i for i, v in enumerate(args, 1) ))
