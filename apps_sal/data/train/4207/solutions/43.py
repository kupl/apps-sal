def sum_cubes(n):
    new = 0
    for num in range(1, n+1):
        new += num ** 3
    return new

