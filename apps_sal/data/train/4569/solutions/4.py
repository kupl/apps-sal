def next_item(xs, item):
  it = iter(xs)
  return next(iter(next(it, None) for x in it if x == item), None)
