def sum_cubes(n):
    count = 0
    for i in range(n + 1):
        count += (i ** 3)
    return count
