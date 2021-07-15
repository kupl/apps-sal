def eval_object(v):
    return {"+": int(v['a'])+int(v['b']),
        "-": v['a']-v['b'],
        "/": v['a']/v['b'],
        "*": v['a']*v['b'],
        "%": v['a']%v['b'],
        "**": v['a']**v['b'], }[v['operation']]
