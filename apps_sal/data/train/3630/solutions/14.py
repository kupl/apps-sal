operators = {'add': int.__add__, 'subtract': int.__sub__, 'multiply': int.__mul__, 'divide': int.__truediv__}


def arithmetic(a, b, op):
    return operators[op](a, b)
