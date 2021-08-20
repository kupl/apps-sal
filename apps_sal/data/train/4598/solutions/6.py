op = {'add': lambda x, y: '{:b}'.format(int(x, 2) + int(y, 2)), 'subtract': lambda x, y: '{:b}'.format(int(x, 2) - int(y, 2)), 'multiply': lambda x, y: '{:b}'.format(int(x, 2) * int(y, 2))}


def calculate(n1, n2, o):
    return op[o](n1, n2)
