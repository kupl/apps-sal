def eval_object(v):
    return {'+': v['a'] + v['b'], '-': int(v['a']) - int(v['b']), '/': int(v['a']) / int(v['b']), '*': int(v['a']) * int(v['b']), '%': int(v['a']) % int(v['b']), '**': int(v['a']) ** int(v['b'])}.get(v['operation'], 1)
