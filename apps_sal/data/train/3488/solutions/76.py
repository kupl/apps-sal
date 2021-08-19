def eval_object(v):
    if v['operation'] == '+':
        return v['a'] + v['b']
    elif v['operation'] == '-':
        return v['a'] - v['b']
    elif v['operation'] == '/':
        return v['a'] / v['b']
    elif v['operation'] == '*':
        return v['a'] * v['b']
    elif v['operation'] == '%':
        return v['a'] % v['b']
    elif v['operation'] == '**':
        return v['a'] ** v['b']
    else:
        return
