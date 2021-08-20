def calculate(num1, operation, num2):
    ops = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}
    try:
        return ops[operation](num1, num2)
    except:
        return None
