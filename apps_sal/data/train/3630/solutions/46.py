a = {'add': '+',
     'subtract': '-',
     'multiply': '*',
     'divide': '/'}


def arithmetic(b, c, d):
    e = a[str(d)]
    f = str(b) + e + str(c)
    return eval(f)
