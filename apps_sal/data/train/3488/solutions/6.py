def eval_object(v):
    return {"+": v['a'] + v['b'],
            "-": v['a'] - v['b'],
            "/": v['a'] / v['b'],
            "*": v['a'] * v['b'],
            "%": v['a'] % v['b'],
            "^": 1,
            "**": v['a']**v['b']}[v['operation']]
