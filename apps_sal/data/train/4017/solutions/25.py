def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def mod(a, b):
    return a % b


def exponent(a, b):
    sum = a
    i = 1
    while i < b:
        sum = a * sum
        i += 1
    return sum


def subt(a, b):
    return a - b


def divide(a, b):
    return a // b
