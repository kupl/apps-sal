def multi_table(number):
    x = list(range(1,11))
    y = ''
    z = 0
    while z < len(x):
        y += '{} * {} = {}\n'.format(x[z], number, x[z] * number)
        z += 1
    return y[:-1]
