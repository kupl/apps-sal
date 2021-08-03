def array_conversion(a, add=True):
    while len(a) > 1:
        a = [x + y if add else x * y for (x, y) in zip(*[iter(a)] * 2)]
        add = not add
    return a[0]
