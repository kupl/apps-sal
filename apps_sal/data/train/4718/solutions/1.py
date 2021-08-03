def fill(i, j, n):
    if i == j or i + j == n - 1:
        return 1
    else:
        return 0


def x(n):
    return [[fill(i, j, n) for j in range(n)] for i in range(n)]
