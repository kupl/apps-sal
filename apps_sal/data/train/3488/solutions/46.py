def eval_object(v):
    return {"+": lambda v: v['a'] + v['b'],
            "-": lambda v: v['a'] - v['b'],
            "/": lambda v: v['a'] / v['b'],
            "*": lambda v: v['a'] * v['b'],
            "%": lambda v: v['a'] % v['b'],
            "**": lambda v: v['a']**v['b'], }[v['operation']](v)
