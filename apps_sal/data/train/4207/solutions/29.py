def sum_cubes(n):
    s = 0
    for i in range(n+1):
        s += pow(i, 3)
    return s
