def sum_cubes(n):
    i = 1
    sums = 0
    while i <= n:
        sums = sums + i ** 3
        i += 1
    return sums
