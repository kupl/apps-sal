def arithmetic(a, b, operator):
    x = [['a','s','m','d'], [a+b,a-b,a*b,a/b]]
    return x[1][x[0].index(operator[0])]

