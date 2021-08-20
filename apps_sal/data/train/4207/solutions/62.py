def sum_cubes(n):
    return sum((x * x * x for x in range(n + 1)))


n = 3
sum_cubes(n)
