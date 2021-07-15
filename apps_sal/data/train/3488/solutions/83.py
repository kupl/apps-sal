def eval_object(v):
    return {
        "+": v['a']+v['b'],
        "-": v['a']-v['b'],
        "/": v['a']/v['b'],
        "*": v['a']*v['b'],
        "%": v['a']%v['b'],
        "**": v['a']**v['b']
       # }.get('operation',1)
        
       }.get(v['operation'])
