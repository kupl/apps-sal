def calculator(x, y, op):
    x = str(x)
    y = str(y)
    if x.isdigit() == True and y.isdigit() == True:
        if op == '+' or op == '-' or op == '*' or (op == '/'):
            equation = x + op + y
            result = eval(equation)
        else:
            result = 'unknown value'
    else:
        result = 'unknown value'
    return result


print(calculator(6, 2, '+'))
print(calculator(4, 3, '-'))
print(calculator(5, 5, '*'))
print(calculator(5, 4, '/'))
print(calculator(6, 2, '&'))
