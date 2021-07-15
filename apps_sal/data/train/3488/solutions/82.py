from operator import add, sub, floordiv, mul, mod, pow

def eval_object(v):
    return {"+": add(v['a'],v['b']),
            "-": sub(v['a'],v['b']),
            "/": floordiv(v['a'],v['b']),
            "*": mul(v['a'],v['b']),
            "%": mod(v['a'],v['b']),
            "**": pow(v['a'],v['b'])}.get(v['operation'])
