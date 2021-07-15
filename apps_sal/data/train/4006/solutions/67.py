def basic_op(operator, value1, value2):
    #your code here
    if operator == '+':
        x = lambda a, b: a+b
        return (x(value1, value2))
    if operator == '-':
        x = lambda a, b: a-b
        return (x(value1, value2))
    if operator == '*':
        x = lambda a, b: a*b
        return (x(value1, value2))
    if operator == '/':
        x = lambda a, b: a/b
        return (x(value1, value2))
