def add(a, b):
    return a + b


def subt(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return a / b
    except:
        return "ZeroDivisionError"


def mod(a, b):
    try:
        return a % b
    except:
        return "ZeroDivisionError"


def exponent(a, b):
    return a ** b

    # Your Code Here

# Make more functions. Refer to the description for function names.
# The code will NOT WORK IF YOU USE names other than the ones
# from the description
