def eval_object(v):
    x = v.get('a')
    y = v.get('b')
    op = v.get('operation')
    return {
        "+": x+y,
        "-": x-y,
        "/": x/y,
        "*": x*y,
        "%": x%y,
        "**": x**y
    }.get(op)
