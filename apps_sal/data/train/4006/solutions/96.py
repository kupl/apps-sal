def basic_op(op, v1, v2):
    if op == '/' and v2 == 0:
        return 'Error! Division by zero!'
    if op not in '+-*/':
        return 'Error! Wrong operator!'
    if op == '+':
        return v1 + v2
    if op == '-':
        return v1 - v2
    if op == '*':
        return v1 * v2
    return v1 / v2
