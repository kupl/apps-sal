def eval_object(v):
    return {'+': int(v['a'] + v['b']), '-': v['a'] - v['b'], '/': v['a'] / v['b'], '*': v['a'] * v['b'], '%': v['a'] % v['b'], '**': v['a'] ** v['b']}.get(v['operation'])
