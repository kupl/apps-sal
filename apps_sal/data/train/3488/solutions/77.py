def eval_object(v):
    output= {"+": v['a']+v['b'],
        "-": v['a']-v['b'],
        "/": v['a']/v['b'],
        "*": v['a']*v['b'],
        "%": v['a']%v['b'],
        "**": v['a']**v['b']}
    return output[v['operation']]  
