def eval_object(v):
    operator = {
        "+": v['a'] + v['b'],
        "-": v['a'] - v['b'],
        "/": v['a'] / v['b'],
        "*": v['a'] * v['b'],
        "%": v['a'] % v['b'],
        "**": v['a']**v['b']
    }
    return operator[v.get('operation', 1)]
