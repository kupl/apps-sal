def eval_object(v):
    return {'+': eval("v['a']+v['b']"), '-': v['a'] - v['b'], '/': v['a'] / v['b'], '*': v['a'] * v['b'], '%': v['a'] % v['b'], '**': v['a'] ** v['b']}.get(v['operation'], 1)
