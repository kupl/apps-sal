def count_feelings(s, arr):
  return next(f'{x} feeling{["s", ""][x == 1]}.' for x in [sum(all(s.count(c) >= x.count(c) for c in x) for x in arr)])
