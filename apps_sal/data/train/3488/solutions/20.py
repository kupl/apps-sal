def eval_object(v):
    return {"+": v.get('a') + v.get('b'),
            "-": v.get('a') - v.get('b'),
            "/": v.get('a') / v.get('b'),
            "*": v.get('a') * v.get('b'),
            "%": v.get('a') % v.get('b'),
            "**": v.get('a')**v.get('b'), }.get(v.get('operation'), 1)
