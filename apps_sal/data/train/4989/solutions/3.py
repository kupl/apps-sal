def hollow_triangle(n):
  return [(f'#{"_" * (2*i-1)}#' if i else '#').center(2*n-1, '_') for i in range(n-1)] + ['#' * (2*n-1)]
