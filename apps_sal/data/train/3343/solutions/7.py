d = {'k': 1, 'm': 2, 'g': 3, 't': 4}


def memorysize_conversion(memorysize):
    (n, u) = memorysize.split(' ')
    n = float(n)
    x = d[u[0].lower()]
    if u[1] == 'i':
        n = round(n * 1.024 ** x, 3)
        return '{} {}{}'.format(n, u[0], u[2]).replace('K', 'k')
    else:
        n = round(n / 1.024 ** x, 3)
        return '{} {}i{}'.format(n, u[0].upper(), u[1])
