def sum_cubes(n):
    g = 0
    for i in range(n + 1):
        i **= 3
        g += i
    return g
