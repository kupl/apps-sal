def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except DivisionZeroError:
        return False


def mod(a, b):
    return a % b


def exponent(a, b):
    return a ** b


def subt(a, b):
    return a - b
