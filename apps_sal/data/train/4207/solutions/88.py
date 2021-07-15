def sum_cubes(n):
    exponentiated = 0
    for count in range(1, n):
        exponentiated += count ** 3
    return exponentiated + n ** 3
