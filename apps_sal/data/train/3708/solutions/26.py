def hex_to_dec(y):
    x, y, z = 16, list(y[::-1]), {'a':'10', 'b':'11', 'c':'12', 'd':'13', 'e':'14', 'f':'15'}
    return sum([int(z[y[i]]) * (x ** i) if y[i] in z else int(y[i]) * (x ** i) for i in range(len(y))])
