def eval_object(v):
    a = {"+": v['a'] + v['b'],
         "-": v['a'] - v['b'],
         "/": v['a'] / v['b'],
         "*": v['a'] * v['b'],
         "%": v['a'] % v['b'],
         "**": v['a']**v['b']}
    return a[v['operation']]
