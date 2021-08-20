import re


def no_order(equation):
    operators = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x // y, '^': lambda x, y: x ** y, '%': lambda x, y: x % y}
    equation = equation.replace(' ', '')
    list_eq = re.split('(\\D)', equation)
    while len(list_eq) != 1:
        x = list_eq.pop(0)
        op = list_eq.pop(0)
        y = list_eq.pop(0)
        try:
            result = operators[op](int(x), int(y))
        except ZeroDivisionError:
            return None
        list_eq.insert(0, result)
    return int(list_eq[0])
