def eval_object(v):
    d = {"+": v['a'] + v['b'],
         "-": v['a'] - v['b'],
         "/": v['a'] / v['b'],
         "*": v['a'] * v['b'],
         "%": v['a'] % v['b'],
         "**": v['a']**v['b'], }
    return d.get(v['operation'])
