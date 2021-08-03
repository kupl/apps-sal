def sum_cubes(n):
    res = 0
    for i in range(1, n + 1):
        res += i ** 3
    return res
