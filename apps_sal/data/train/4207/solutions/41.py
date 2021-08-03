def sum_cubes(n):
    c = 0
    for i in range(1, n + 1):
        c = c + i**3
    return c
