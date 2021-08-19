def vampire_test(x, y):
    return sorted(f'{x}{y}') == sorted(f'{x * y}')
