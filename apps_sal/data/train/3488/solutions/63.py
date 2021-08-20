def eval_object(v):
    sw = {'+': v['a'] + v['b'], '-': v['a'] - v['b'], '/': v['a'] / v['b'], '*': v['a'] * v['b'], '%': v['a'] % v['b'], '**': v['a'] ** v['b']}
    return sw.get(v['operation'])
