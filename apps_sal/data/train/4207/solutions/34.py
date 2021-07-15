def sum_cubes(n):
    total = 0
    for x in range(n+1):
        total += x**3
    return total
