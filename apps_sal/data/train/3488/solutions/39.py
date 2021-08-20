def eval_object(v):
    b = v['operation']
    a = {'+': v['a'] + v['b'], '-': v['a'] - v['b'], '/': v['a'] / v['b'], '*': v['a'] * v['b'], '%': v['a'] % v['b'], '**': v['a'] ** v['b']}
    return a[b]
