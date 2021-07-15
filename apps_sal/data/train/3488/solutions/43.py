def eval_object(v):
    dict = {'+': v['a']+v['b'],
    '-': v['a']-v['b'],
    '/': v['a']/v['b'],
    '*': v['a']*v['b'],
    '%': v['a']%v['b'],
    '**': v['a']**v['b']}
    return dict.get (v.get('operation'))
