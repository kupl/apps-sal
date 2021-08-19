def x(n):
    return [[int(i == j or i == n - j - 1) for i in range(n)] for j in range(n)]
