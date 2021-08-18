def sum_cubes(n):
    sum_cube = 0
    for e in range(0, n + 1):
        sum_cube += e**3
    return sum_cube
