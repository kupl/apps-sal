def sort_transform(a):
  return '-'.join([''.join(map(chr, x[:2]+x[-2:])) for x in [a, sorted(a), sorted(a, reverse=1), sorted(a, key=chr)]])
