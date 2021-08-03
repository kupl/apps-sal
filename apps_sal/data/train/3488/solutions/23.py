def eval_object(v):

    x = {"+": v['a'] + v['b'],

         "-": v['a'] - v['b'],
         "/": v['a'] / v['b'],
         "*": v['a'] * v['b'],
         "%": v['a'] % v['b'],

         "**": v['a']**v['b']}

    if v['operation'] in x:

        return x.get(v['operation'])
