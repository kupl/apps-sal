def sum_cubes(n):
    a = 0
    for x in range(1, n + 1):
        a = x ** 3 + a
    return a
