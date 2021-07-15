def eval_object(v):
    print(v)
    return {
        "+": v['a']+v['b'],
        "-": v['a']-v['b'],
        "/": v['a']/v['b'],
        "*": v['a']*v['b'],
        "%": v['a']%v['b'],
        "**": v['a']**v['b'], }.get(v['operation'])
