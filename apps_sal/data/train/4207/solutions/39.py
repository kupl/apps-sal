def sum_cubes(n):
    total = 0
    for i in range(1, n + 1):
        i = i ** 3
        total += i
    return total

