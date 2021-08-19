def basic_op(operator, value1, value2):
    if operator == '+':
        res = value1 + value2
        return res
    elif operator == '-':
        res = value1 - value2
        return res
    elif operator == '*':
        res = value1 * value2
        return res
    elif operator == '/':
        res = value1 / value2
        return res
    else:
        print('Use only (+ - * /) functions')
