def sum_cubes(n):
    values = range(1, n + 1)
    s = 0
    for value in values:
        cubed = value ** 3
        s += cubed
    return s
