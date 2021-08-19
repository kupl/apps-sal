def eval_object(v):
    if v['operation'] == '+':
        return int(v['a']) + int(v['b'])
    elif v['operation'] == '-':
        return int(v['a']) - int(v['b'])
    elif v['operation'] == '/':
        return int(v['a']) / int(v['b'])
    elif v['operation'] == '*':
        return int(v['a']) * int(v['b'])
    elif v['operation'] == '%':
        return int(v['a']) % int(v['b'])
    elif v['operation'] == '**':
        return int(v['a']) ** int(v['b'])
