def arithmetic(a, b, operator):
    op = {
        'add': '+',
        'subtract': '-',
        'multiply': '*',
        'divide': '/'
    }
    return eval("{} {} {}".format(a, op[operator], b))
