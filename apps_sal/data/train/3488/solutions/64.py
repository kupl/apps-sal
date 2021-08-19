def eval_object(v):
    switcher = {'+': v['a'] + v['b'], '-': v['a'] - v['b'], '/': v['a'] / v['b'], '*': v['a'] * v['b'], '%': v['a'] % v['b'], '**': v['a'] ** v['b']}
    return switcher.get(v['operation'], 1)
