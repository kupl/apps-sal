def eval_object(v):
    a = v['a']
    b = v['b']
    c = v['operation']
    if c == '+':
        return(int(a) + int(b))
    elif c == '-':
        return(int(a) - int(b))
    elif c == '/':
        return(int(a) / int(b))
    elif c == '*':
        return(int(a) * int(b))
    elif c == '%':
        return(int(a) % int(b))
    elif c == '**':
        return(int(a) ** int(b))
