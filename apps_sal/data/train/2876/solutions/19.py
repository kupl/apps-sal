def check(a, x):
    return x in range(a[0], a[1] + 1) if type(a) == 'int' else x in a
