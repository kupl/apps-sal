def min_dot(a, b):
  dot = lambda xs, ys: sum(x*y for x,y in zip(xs, ys))
  return dot(sorted(a), sorted(b, reverse=True))
