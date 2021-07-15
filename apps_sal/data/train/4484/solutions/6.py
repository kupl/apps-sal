from operator import add, sub, mul
def calculate(num1, operation, num2): 
    d = {'+': add, '-': sub, '*': mul, '/': lambda a, b: a / b if b else None}
    return d.get(operation, lambda a, b: None)(num1, num2)
