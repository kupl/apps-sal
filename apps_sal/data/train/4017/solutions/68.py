def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def divide(a, b):
    ans = ''
    try:
        ans = a / b
    except ZeroDivisionError:
        print('division by zero')
    else:
        return ans


def mod(a, b):
    return a % b


def subt(a, b):
    return a - b


def exponent(a, b):
    return a ** b
