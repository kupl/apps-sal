import re


def no_order(equation):
    # Delete blank spaces
    equation = equation.replace(' ', '')

    # Check null cases
    if '%0' in equation or '/0' in equation:
        return None

    # Extract numbers and operators
    n = re.findall(r'\d+', equation)
    op = re.findall('[+\\-*/%^]', equation)

    # Define operators
    operators = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x // y,
        "^": lambda x, y: x ** y,
        "%": lambda x, y: x % y}

    result = int(n[0])
    for i in range(1, len(n)):
        result = operators[op[i - 1]](result, int(n[i]))
    return result
