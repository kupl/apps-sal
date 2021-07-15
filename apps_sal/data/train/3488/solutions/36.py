def eval_object(v):
    operations = {
        "+": v['a'] + v['b'],
        "-": v['a'] - v['b'],
        "/": v['a'] / v['b'],
        "*": v['a'] * v['b'],
        "%": v['a'] % v['b'],
        "**": v['a'] ** v['b']
    }

    return operations.get(v['operation'], 1)

