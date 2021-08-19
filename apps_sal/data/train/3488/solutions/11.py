def eval_object(v):
    if v['operation'] == '+':
        c = v['a'] + v['b']
        return c
    if v['operation'] == '-':
        c = v['a'] - v['b']
        return c
    if v['operation'] == '/':
        c = v['a'] / v['b']
        return c
    if v['operation'] == '*':
        c = v['a'] * v['b']
        return c
    if v['operation'] == '%':
        c = v['a'] % v['b']
        return c
    if v['operation'] == '**':
        c = v['a'] ** v['b']
        return c
