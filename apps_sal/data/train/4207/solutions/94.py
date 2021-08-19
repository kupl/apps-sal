def sum_cubes(n):
    res = 1
    while n > 1:
        res += n * n * n
        n -= 1
    return res
