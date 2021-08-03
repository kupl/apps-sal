def add(a, b):
    if a != str(a) or b != str(b):
        return a + b
    return a + ' + ' + b


def multiply(a, b):
    if a != str(a) or b != str(b):
        return a * b
    return a + ' * ' + b


def divide(a, b):
    if a != str(a) or b != str(b):
        return a / b
    return a + ' / ' + b


def mod(a, b):
    if a != str(a) or b != str(b):
        return a % b
    return a + ' % ' + b


def exponent(a, b):
    if a != str(a) or b != str(b):
        return a ** b
    return a + ' ** ' + b


def subt(a, b):
    if a != str(a) or b != str(b):
        return a - b
    return a + ' - ' + b
