def eval_object(v):
    c = {'+': v['a'] + v['b'], '-': v['a'] - v['b'], '/': v['a'] / v['b'], '*': v['a'] * v['b'], '%': v['a'] % v['b'], '**': v['a'] ** v['b']}
    if v.get('operation') == '+':
        return v.get('a') + v.get('b')
    elif v.get('operation') == '-':
        return v.get('a') - v.get('b')
    elif v.get('operation') == '*':
        return v.get('a') * v.get('b')
    elif v.get('operation') == '**':
        return v.get('a') ** v.get('b')
    elif v.get('operation') == '/':
        return v.get('a') / v.get('b')
    elif v.get('operation') == '%':
        return v.get('a') % v.get('b')
    else:
        return None
