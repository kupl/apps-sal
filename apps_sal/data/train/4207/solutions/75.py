def sum_cubes(n):
    y = n + 1
    x = list(range(0, y))
    z = []
    for i in x:
        a = i ** 3
        z.append(a)
    return sum(z)
