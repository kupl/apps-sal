def eval_object(v):
    op = {'+': v['a'] + v['b'], '-': v['a'] - v['b'], '/': v['a'] / v['b'], '*': v['a'] * v['b'], '%': v['a'] % v['b'], '**': v['a'] ** v['b']}
    a = v.get('operation')
    return op[a]
