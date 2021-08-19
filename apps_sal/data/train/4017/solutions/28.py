import operator


def add(a, b):
    # print(dir(operator))
    return operator.__add__(a, b)


def multiply(a, b):
    return operator.__mul__(a, b)


def divide(a, b):
    return operator.__floordiv__(a, b)


def mod(a, b):
    return operator.__mod__(a, b)


def exponent(a, b):
    return operator.__pow__(a, b)


def subt(a, b):
    return operator.__sub__(a, b)
