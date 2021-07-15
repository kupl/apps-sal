def eval_object(v):
    def add(d):
        return d['a'] + d['b']
    def subtract(d):
        return d['a'] - d['b']
    def divide(d):
        return d['a'] / d['b']
    def remainder(d):
        return d['a'] % d['b']
    def multiply(d):
        return d['a'] * d['b']
    def double_star(d):
        return d['a'] ** d['b']
    return {"+": add(v),
            "-": subtract(v),
            "/": divide(v),
            "*": multiply(v),
            "%": remainder(v),
            "**": double_star(v) }.get(v['operation'])
