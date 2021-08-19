def sum_cubes(n):
    result = 0
    for i in range(0, n + 1):
        cube = i ** 3
        result += cube
    return result
