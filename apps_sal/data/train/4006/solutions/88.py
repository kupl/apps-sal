def basic_op(operator, v1, v2):
    if operator == '-':
        new = v1 - v2

    elif operator == '+':
        new = v1 + v2

    elif operator == '*':
        new = v1 * v2

    else:
        new = v1 / v2

    return new
