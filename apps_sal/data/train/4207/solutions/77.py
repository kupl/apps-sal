def sum_cubes(n):
    a = 0
    for i in range(n + 1):
        a = i * i * i + a
        i += 1
    return a
