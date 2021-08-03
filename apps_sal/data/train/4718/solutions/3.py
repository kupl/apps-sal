def x(n): return [[1 if y == x or y == n - x - 1 else 0 for y in range(n)] for x in range(n)]
