def eval_object(v):
    a = v['a']
    b = v['b']
    c = v['operation']
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    elif c == '/':
        return a / b
    elif c == '%':
        return a % b
    elif c == '**':
        return a ** b
