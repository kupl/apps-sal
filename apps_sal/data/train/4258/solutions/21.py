def series_sum(n):
  return '%.2f' % sum(1/x for x in range(1, n*3+1, 3))
