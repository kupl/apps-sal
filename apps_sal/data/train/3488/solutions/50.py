def eval_object(v):
   # return {"+": v['a']+v['b'],
    #         "-": v['a']-v['b'],
    #         "/": v['a']/v['b'],
    #         "*": v['a']*v['b'],
    #         "%": v['a']%v['b'],
    #         "**": v['a']**v['b'], }.get('operation',1)
    a = v.get('a')
    op = v.get('operation')
    b = v.get('b')
    all = str(a) + op + str(b)
    return eval(all)
