def x(n):
    return [[1 if i == j or i + j + 1 == n else 0 for i in range(n)] for j in range(n)]
