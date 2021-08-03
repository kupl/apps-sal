def add(a, b):
    return a + b


def multiply(a, b):
    result = 0
    for i in range(b):
        result += a
    return result


def divide(a, b):
    return a / b


def mod(a, b):
    while a >= b:
        a -= b
    return a


def exponent(a, b):
    result = a
    for i in range(b - 1):
        result *= a
    return result


def subt(a, b):
    return a - b
