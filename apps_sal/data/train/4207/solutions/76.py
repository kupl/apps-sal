def sum_cubes(n):
    res = 0
    if n > 0:
        for x in range(1, n + 1):
            res += x ** 3
    return res
