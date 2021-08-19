def shape_area(n):
  # 1 1
  # 2 5 1 + 3 + 1
  # 3 13 1 + 3 + 5 + 3 + 1
  # 4 25 1 + 3 + 5 + 7 + 5 + 3 + 1
    return 2 * sum(x for x in range(1, 2 * (n - 1), 2)) + (2 * n - 1)
