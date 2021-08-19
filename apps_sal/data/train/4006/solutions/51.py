def basic_op(operator, v1, v2):
    if operator == '+':
        a1 = v1 + v2
    elif operator == '-':
        a1 = v1 - v2
    elif operator == '*':
        a1 = v1 * v2
    elif operator == '/':
        a1 = v1 / v2
    else:
        print('You have not typed a valid operator, please run the program again.')
    return a1
