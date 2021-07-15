eval_object = lambda v: {
    '+':  v['a'] +  v['b'],
    '-':  v['a'] -  v['b'],
    '/':  v['a'] /  v['b'],
    '*':  v['a'] *  v['b'],
    '%':  v['a'] %  v['b'],
    '**': v['a'] ** v['b']
}.get(v['operation'], 0)
