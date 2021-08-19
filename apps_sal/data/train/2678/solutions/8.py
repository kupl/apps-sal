import re


def no_order(equation):
    equation = equation.replace(' ', '')
    if '%0' in equation or '/0' in equation:
        return None
    n = re.findall('\\d+', equation)
    op = re.findall('[+\\-*/%^]', equation)
    operators = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x // y, '^': lambda x, y: x ** y, '%': lambda x, y: x % y}
    result = int(n[0])
    for i in range(1, len(n)):
        result = operators[op[i - 1]](result, int(n[i]))
    return result
