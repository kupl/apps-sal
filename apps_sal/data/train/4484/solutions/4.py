from operator import add, sub, mul, truediv
D = {'+': add, '-': sub, '*': mul, '/': truediv}


def calculate(num1, operation, num2):
    try:
        return D[operation](num1, num2)
    except (ZeroDivisionError, KeyError):
        return
