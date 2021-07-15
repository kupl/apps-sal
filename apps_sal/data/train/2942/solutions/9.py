def fold_to(distance):
  if distance >= 0: return next(i for i in __import__('itertools').count() if 1e-4*2**i >= distance)
