def x(n):
    return [[int(c == r or c == n - r - 1) for c in range(n)] for r in range(n)]
