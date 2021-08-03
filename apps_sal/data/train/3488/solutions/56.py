def eval_object(v):
    Oper = {"+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: a / b,
            "*": lambda a, b: a * b,
            "%": lambda a, b: a % b,
            "**": lambda a, b: a ** b}
    return Oper[v['operation']](v['a'], v['b'])
