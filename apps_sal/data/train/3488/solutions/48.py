def eval_object(v):
    c = v['operation']
    a = v['a']
    b = v['b']
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '/':
        return a / b
    elif c == '*':
        return a * b
    elif c == '%':
        return a % b
    else:
        return a ** b
