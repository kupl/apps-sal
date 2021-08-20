def eval_object(v):
    a = v.get('a')
    b = v.get('b')
    op = v.get('operation')
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '/':
        return a / b
    elif op == '*':
        return a * b
    elif op == '%':
        return a % b
    elif op == '**':
        return a ** b
